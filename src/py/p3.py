import math
a = int(input())
b = int(input())
s = []
while b >=a:
    s.append(b)
    if b==a:
        print("YES")
        print(len(s))
        print(*s[::-1])
        break
    if b% 2==0:
        b = b // 2
    elif b% 10==1:
        b=(b-1) // 10

    else:
        print("NO")
        break
