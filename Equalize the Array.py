n = int(input())

arr = list(map(int, input().rstrip().split()))

counter=0
for i in arr:
    curr = arr.count(i)
    if (curr > counter):
        counter = curr

if n-counter < n:
    print(n-counter)
else:
    print(counter)
