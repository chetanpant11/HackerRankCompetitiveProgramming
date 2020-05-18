akq = list(map(int, input().rstrip().split()))

value = list(map(int, input().rstrip().split()))

new_arr = value[-akq[1]%len(value):] + value[:-akq[1]%len(value)]
#value1=value[-akq[1]:]+value[:akq[1]-1]

for i in range(0, akq[2]):
    b = int(input())
    print(new_arr[b])
