nd = input().split()

n = int(nd[0])

d = int(nd[1])

arr = list(map(int, input().rstrip().split()))
ll=[]
for i in range(n):
    l = []
    a=i
    for j in range(i+1, min(i + d + d + 1, n)):
        if abs(arr[a]-arr[j])==d and len(l)<3:
            l.append(arr[a])
            l.append(arr[j])
            a=j
        else:
            continue
    q=set(l)
    if len(q)==3:
        ll.append(l)

print(len(ll))
