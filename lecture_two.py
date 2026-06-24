print("hello world")
str = "i am studying python"
print(str.endswith("hon"))#returns true if string ends with substr
print(str.capitalize())#capitalizes 1st char
str = str.capitalize()
print(str)
print(str.replace("o","a"))#replaces all occurences of old value
print(str.replace("python","java"))
print(str.count("i"))

#conditional statemnets
#if-elif-else(syntax) #if is always check # condition depend # else are always in last 
age = 23

if(age >= 18):
    print("can vote & apply for license")

light = "black"

if(light == "red"):
    print("stop") #indentation means proper spacing
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("wait")
else:
    print("light is broken")

print("end of code")

#Question
# conditional statements

marks = int(input("enter student marks :"))

if(marks >= 90):
    grade ="A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"
print("great of the student ->", grade)

#nesting statement and under ek or statement
age = 34

if(age >= 18):
    if(age >= 80):
        print("cannot dirve")
    print("can drive")
else:
    print("cannot drive")
