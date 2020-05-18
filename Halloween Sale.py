pdms = input().split()

p = int(pdms[0])

d = int(pdms[1])

m = int(pdms[2])

s = int(pdms[3])

e=0

while s>=p:
    e = e+1
    s-=p
    p=max(p-d, m)

print(e)