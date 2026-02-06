#position of max
n = int(input())
a = input().split()  
for i in range(n):
    a[i] = int(a[i])  
maxvalue=a[0]  
maxindex=0  
for i in range(n):
    if a[i] > maxvalue:
        maxvalue = a[i]
        maxindex = i 
print(maxindex + 1)  
