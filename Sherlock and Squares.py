import math

q=int(input())

for i in range(1, q+1):
    z=0
    ab = input().split()
    a=int(ab[0])
    b=int(ab[1])
    res = math.ceil(math.sqrt(a))
    while res*res <= b:
        z = z+1
        res=res+1
    print(z)
