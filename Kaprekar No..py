p = int(input())

q = int(input())
ppp=[]
for i in range(p, q):
    b=0
    u=0
    w=0
    n=i*i
    pp=[10,100,1000,10000,100000]
    while n>0:
        rem=n%10
        n=n//10
        if (rem+n==i or n+b==i) and (i not in pp):
            print(i,end=" ")
            ppp.append(i)

        else:
            w = n % 10
            if b < rem:
                u = str(w) + str(rem)
            else:
                u = str(w) + str(u)
            b=int(u)
            continue
print(len(ppp))