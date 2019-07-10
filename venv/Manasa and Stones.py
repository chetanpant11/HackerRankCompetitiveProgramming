T = int(input())

for T_itr in range(T):
    n = int(input())

    a = int(input())

    b = int(input())
    list1=[]
    for i in range(n):
        list1.append((i*a)+(n-i-1)*b)

    set1=set(list1)
    list2=list(set1)
    list2.sort()
    list3=map(str, list2)
    print(" ".join(list3))

