a = int(input())
p = list(map(int, input().rstrip().split()))

value = []
for i in range(1, a+1):
    b = p.index(i)
    value.append(b+1)


for i in value:
    c=p.index(i)
    print(c+1)
