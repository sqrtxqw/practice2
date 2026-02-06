n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
min_value = a[0]
max_value = a[0]
for i in a:
    if i < min_value:
        min_value = i
    if i > max_value:
        max_value = i
for i in range(n):
    if a[i] == max_value:
        a[i] = min_value
for i in a:
    print(i, end=" ")
