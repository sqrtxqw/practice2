#strings
n = int(input())
a = [input() for _ in range(n)]
unique = []
for x in a:
    if x not in unique:
        unique.append(x)
unique.sort()
for x in unique:
    print(x, a.index(x) + 1)

