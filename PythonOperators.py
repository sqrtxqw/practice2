#Python Operators
print(10 + 5)

sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)

#Arithmetic Operators
x = 15
y = 4
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#Assignment Operators
numbers = [1, 2, 3, 4, 5]
if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

#Comparison Operators
x = 5
print(1 < x < 10)
print(1 < x and x < 10)

#Logical Operators
x = 5
print(x > 0 and x < 10)

#Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) #True
print(x is y) #False
print(x == y) #True

#Membership Operators
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

#Bitwise Operators
print(6 & 3) #2
print(6 | 3) #7
print(6 ^ 3) #5

