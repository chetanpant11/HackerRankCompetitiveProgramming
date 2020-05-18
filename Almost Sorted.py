n = int(input())

arr = list(map(int, input().rstrip().split()))
flag=True
arr1=list(arr)
arr1.sort()
l=[]
for i in range(n):
    if arr1[i]!=arr[i]:
        l.append(i)

if len(l)==0:
    print("yes\n")
elif len(l)==2:
    print("yes\nswap",l[0]+1,l[1]+1)
else:
    first=l[0]
    second=l[-1]
    while(first<second):
        arr[first],arr[second]=arr[second],arr[first]
        first+=1
        second-=1
    for i in range(n):
        if (arr1!=arr):
            print("no")
            break
    print("yes\nrevese", l[0]+1, l[len(l)-1]+1 )

