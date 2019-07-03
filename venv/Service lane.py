nt = input().split()

n = int(nt[0])

t = int(nt[1])

width = list(map(int, input().rstrip().split()))

cases = []

for _ in range(t):
    cases.append(list(map(int, input().rstrip().split())))
l=[]
for i in range(t):  
    a=min(width[cases[i][0]:cases[i][1]+1])
    l.append(a)
print(l)
