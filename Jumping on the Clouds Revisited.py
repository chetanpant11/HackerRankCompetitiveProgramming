nk = list(map(int, input().rstrip().split()))
l = list(map(int, input().rstrip().split()))

e = 100
c=0
a=0
for i in range(0, nk[0]):

    a = ((c+nk[1])%nk[0])
    c=c+nk[1]
    if c>nk[0]:
        break
    else:
        if l[a]==0:
            e = e-1

        elif l[a]==1:
            e = e-1-2

print(e)
