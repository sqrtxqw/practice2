#max of int
n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
s = a[0]
for i in a:
    if i>s:
        s=i
print(s)
