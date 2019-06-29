s = input()

n = int(input())
c=0
q=0
a=n%len(s)
b=n//len(s)
for i in range(0, len(s)):
    if s[i]=='a':
        c=c+1
    if s[i]=='a' and i<a:
        q=q+1
print((b*c)+q)
