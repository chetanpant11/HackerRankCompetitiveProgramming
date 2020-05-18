T = int(input())

for T_itr in range(T):
    w = list(input())
    i = len(w)-1
    while i>0 and w[i-1]>=w[i]:
        i -= 1
    if i<=0:
        print("no answer")
        continue
    j= len(w)-1
    while w[j] <= w[i-1]:
        j-=1
    w[i - 1], w[j] = w[j],w[i - 1]

    w[i:]=w[len(w)-1 : i-1: -1]
    print("".join(w))