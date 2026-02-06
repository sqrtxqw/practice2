#count all positive integers
n = int(input())
a = input().split()
s = 0
for i in a:
    if int(i)>0:
        s += 1
print(s)
