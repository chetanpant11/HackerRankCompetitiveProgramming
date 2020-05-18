t = int(input())

for t_itr in range(t):
    ncm = input().split()

    n = int(ncm[0])

    c = int(ncm[1])

    m = int(ncm[2])

    a = n//c
    t=a
    while t>=m:
        a=a+1
        t-=m
        t=t+1
    print(a)