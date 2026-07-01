info1 ={
    "key" : "value",
    "name" : "ujwal",
    "learning" : "coding"
}
print(info1)

info = {
    "age" : 35,
    "name" : "ujwal",
    "marks" : 98.45
}
print(info)
print(info1["name"])
print(info1["learning"])

null_dict = {}
null_dict["name"] = "ujwal vijay daivikar"
print(null_dict)


#nested dictionaries
student = {
    "name" : "ujwal daivikar",
    "subject" : {
        "phy" : 97,
        "chem" : 67,
        "maths" : 98, 
    }
}
print(student)
print(student["subject"]["chem"])
print(student["subject"]["maths"])
print(student.keys[])