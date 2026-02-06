#contacts
n = int(input())
numbers = [input().strip() for _ in range(n)]
count = 0
for num in set(numbers):
    if numbers.count(num) == 3:
        count += 1
print(count)
