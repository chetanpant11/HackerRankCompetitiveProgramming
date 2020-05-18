import math
s = input()
q=s.replace(" ","")
a=len(s)
b=math.floor(math.sqrt(a))
c=math.ceil(math.sqrt(a))
str=""
d=0
j=0
for i in range(0 ,c):
    j=i
    while(j<len(s)):
        print(s[j], end="")
        j=j+c
    print(" ", end="")
