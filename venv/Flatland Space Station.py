nm = input().split()

n = int(nm[0])

m = int(nm[1])

c = list(map(int, input().rstrip().split()))

ans=0
if n==m:
    print(0)
c.sort()
print(c)
for i in range(m-1):
    ans=max(ans, abs(c[i]-c[i+1]//2))
    ans=max(max(ans, c[0]),(n-1)-c[-1])
print(ans)