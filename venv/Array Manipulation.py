nm = input().split()

n = int(nm[0])

m = int(nm[1])

queries = []

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))

d=[0 for i in range(n)]
# print(queries[0][0])
for i in range(m):
    d[(queries[i][0])-1]+=queries[i][2]
    if (queries[i][1])!=n:
        d[(queries[i][1])] -= (queries[i][2])
# print(d)

for i in range(1,n):
    d[i]=d[i]+d[i-1]

print(max(d))
