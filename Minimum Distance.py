n = int(input())

a = list(map(int, input().rstrip().split()))
l=[]
for i in range(0, n):
    for j in range(i+1, n):
        if a[i]==a[j]:
            b=a.index(a[i])
            c=a.index(a[j],i+1)
            l.append(c-b)
            break
        else:
            continue
if len(l)>0:
    print(min(l))
else:
    print("-1")

