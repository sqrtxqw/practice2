#is it prime
import math
n = int(input())
if n <= 1:
    print("No")
else:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print("No")
            break
    else:
        print("Yes")
