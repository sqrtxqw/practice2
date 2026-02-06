#Reverse elements from exttt{l} to exttt{r}
n, l, r = input().split()
n = int(n)
l = int(l)
r = int(r)
a = input().split()
l -= 1
r -= 1
a[l:r+1] = a[l:r+1][::-1]
for x in a:
    print(x, end=" ")
