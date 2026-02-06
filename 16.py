#newbie
n = int(input())
a = input().split()
arr = []  
for x in a:
    if x not in arr:
        print("YES")
        arr.append(x)
    else:
        print("NO")
