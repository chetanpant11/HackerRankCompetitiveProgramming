d1M1Y1 = input().split()

d1 = int(d1M1Y1[0])

m1 = int(d1M1Y1[1])

y1 = int(d1M1Y1[2])

d2M2Y2 = input().split()

d2 = int(d2M2Y2[0])

m2 = int(d2M2Y2[1])

y2 = int(d2M2Y2[2])

if d1!=d2 and m1==m2 and y1==y2 and d2<d1:
    a=d2-d1
    b=a*15
    print(abs(b))

elif m1!=m2 and y1==y2 and m2<m1:
    a=m2-m1
    b=a*500
    print(abs(b))

elif y1!=y2 and y2<y1:
    b=10000
    print(abs(b))

else:
    print(0)
