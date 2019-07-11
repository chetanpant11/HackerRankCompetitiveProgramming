g = int(input())
for g_itr in range(g):
    n = int(input())

    b = input()
    flag = True
    c=b.count("_")
    if c>=1:
        for i in range(len(b)):
            if c==len(b):
                flag=True
                break
            elif b[i]=="_":
                continue
            else:
                p=b.count(b[i])
                if p==1:
                    flag=False
                    break
                else:
                    flag=True
    else:
        for i in range(len(b)):
            if len(b)!=1:
                if (i == 0 and b[i] != b[i + 1]) or (i == n - 1 and b[i] != b[i - 1]) or (
                        b[i] != b[i - 1] and b[i] != b[i + 1]):
                    flag=False
            else:
                flag=False

    if flag==True:
        print("YES")
    else:
        print("NO")
