a =(1, 45, 345, False, "Rohan", "shivam")
# a[0] = 453 cannot change the tuple 
print((a))


no = a.count(45)
print(no)

# tuple itself has only 2 methods:
# 1. Count()
numbers = (10,20,10,30,10)
print(numbers.count(10))

# 2. index()
fruits = ("apple", "banana", "mango" , "banana")
print(fruits.index("banana"))

students = ("ram", "shyam", "Hari", "ram")
print(students.count("ram"))
print(students.index("hari"))
