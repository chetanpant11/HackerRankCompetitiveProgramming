n = int(input())

c = list(map(int, input().rstrip().split()))
count=0
i=0
while i < n-1:
    if i+2<n and c[i+2]==0:
        count=count+1
        i=i+2
    else:
        if c[i]==0 and c[i+1]==0:
            count=count+1
            i=i+1

print(count)
