t = int(input())
for t_itr in range(t):
    count = 0
    n = int(input())
    b=n
    while b>0:
        a = b%10
        b=b//10
        if a!=0 and n%a==0:
            count=count+1
        else:
            continue

    print(count)
