t = int(input())

for t_itr in range(t):
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])
    a=[]
    flag=True
    s=set(range(1, n+1))
    for i in range(1, n+1):

        if i<=k and i in range(1,k+1):
            if (i+k) in s:
                a.append(i+k)
                s.remove(i+k)
                flag=True
            # elif (i+k) in range(1, n+1) and i+k in a:
            #     a.append(i+k)
            #     flag=True

            else:
                flag=False
        else:
            if (i - k) in s:
                a.append(i-k)
                s.remove(i - k)
                flag=True
            elif (i+k) in s :
                a.append(i+k)
                s.remove(i + k)
                flag=True
            else:
                flag=False



    if flag==True and len(a)==n:
        b=map(str, a)
        print(' '.join(b))
    else:
        print("-1")