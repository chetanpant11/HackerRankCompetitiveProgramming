t = int(input())

for t_itr in range(t):
    flag=False
    RC = input().split()

    R = int(RC[0])

    C = int(RC[1])

    G = []

    for _ in range(R):
        G_item = input()
        G.append(G_item)

    rc = input().split()

    r = int(rc[0])

    c = int(rc[1])

    P = []

    for _ in range(r):
        P_item = input()
        P.append(P_item)

    for i in range(R-(r)):
        for j in range(C-(c)+1):
            t=0
            a=[]
            while(t<r):
                a.append(G[i+t][j:c+j])
                t=t+1
            if a==P:
                flag=True
            else:
                continue

    if flag==True:
        print("YES")
    else:
        print("NO")
