n = int(input())
arr = list(map(int, input().rstrip().split()))
for i in arr:
    if len(arr)!=0:
        print(len(arr))
        c=min(arr)
        a = list(map(lambda x: x - c, arr))
        arr=a
        arr.sort()
        while 0 in arr:
            arr.remove(0)
    else:
            break
