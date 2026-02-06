#Boolean Values
print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False

#Evaluate Values and Variables
print(bool("Hello")) #True
print(bool(15)) #True

#Most Values are True
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#Some Values are False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#Functions can Return a Boolean
def myFunction() :
  return True
print(myFunction())