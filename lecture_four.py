#lists & tuples
marks = [94.98, 87.89, 78.98, 45.78]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])

student = ["ujwal", 93.9, 23,"yavatmal"]
print(student)
print(student[0])
print(student[3])
print(student[2])
student[0] = "rudra"
print(student[0])
#lists slicing
marks = [67,89,37,64]
print(marks[1:4])
print(marks[-3:-1])

list = [1,2,5,8]
print(list.append(4))
print(list.sort(reverse=True))
print(list)

list1= ['b', 'c', 'd', 'a']
print(list1.sort(reverse=True))

#tuples
#A built in data type that lets use create immutable sequences of values
tup = (4,9,5,6,2,)
print(tup[0])
print(tup[2])
print(tup.count(2))