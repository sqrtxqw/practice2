#Most Frequent Element
n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
max_count = 0
answer = a[0]
for i in range(n):
    count = 0
    for j in range(n):
        if a[j] == a[i]:
            count += 1
    if count > max_count or (count == max_count and a[i] < answer):
        max_count = count
        answer = a[i]
print(answer)
