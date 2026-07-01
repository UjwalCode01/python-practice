from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime, timedelta
from fastapi.responses import HTMLResponse
import sqlite3
import os

app = FastAPI(title="Duplicate Payment Prevention System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_FILE = "payments.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            vendor_id TEXT,
            amount REAL,
            timestamp TEXT,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

class PaymentRequest(BaseModel):
    user_id: str
    amount: float
    vendor_id: str

@app.post("/process-payment")
async def process_payment(payment: PaymentRequest):
    current_time = datetime.now()
    current_time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    two_minutes_ago = (current_time - timedelta(minutes=2)).strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute('''
        SELECT timestamp FROM transactions 
        WHERE user_id=? AND amount=? AND vendor_id=? AND timestamp >= ?
    ''', (payment.user_id, payment.amount, payment.vendor_id, two_minutes_ago))
    
    past_tx = cursor.fetchone()
    
    if past_tx:
        past_time = datetime.strptime(past_tx[0], "%Y-%m-%d %H:%M:%S")
        time_difference = current_time - past_time
        conn.close()
        raise HTTPException(
            status_code=400, 
            detail=f"Duplicate Transaction Blocked! Please wait {int(120 - time_difference.total_seconds())} seconds."
        )
    
    cursor.execute('''
        INSERT INTO transactions (user_id, vendor_id, amount, timestamp, status)
        VALUES (?, ?, ?, ?, ?)
    ''', (payment.user_id, payment.vendor_id, payment.amount, current_time_str, "Success"))
    
    conn.commit()
    conn.close()
    
    return {
        "status": "Success", 
        "message": "Payment Processed Successfully!",
        "data": {
            "user_id": payment.user_id,
            "amount": payment.amount,
            "vendor_id": payment.vendor_id,
            "time": current_time.strftime("%H:%M:%S")
        }
    }

@app.get("/transactions")
async def get_all_transactions():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, user_id, vendor_id, amount, status FROM transactions")
    rows = cursor.fetchall()
    conn.close()
    
    history = []
    for row in rows:
        history.append({
            "timestamp": row[0],
            "user_id": row[1],
            "vendor_id": row[2],
            "amount": row[3],
            "status": row[4]
        })
    return history

@app.get("/", response_class=HTMLResponse)
async def serve_homepage():
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>index.html file not found!</h1>"