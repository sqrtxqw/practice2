#Set
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Access Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Add Items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#Remove Item
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") #discard
print(thisset)

#Loop Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Join Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2 #set3 = set1.union(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2) #&
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2) #-
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2) #^
print(set3) #{'google', 'banana', 'microsoft', 'cherry'}

#Python frozenset  is an immutable version of a set.
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
