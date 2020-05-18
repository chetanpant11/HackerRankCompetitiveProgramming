nk = input().split()

n = int(nk[0])

k = int(nk[1])

arr = list(map(int, input().rstrip().split()))

cnt = 0
pageNum = 1
for chapter in arr:
    pages = (chapter + k - 1) // k
    for i in range(pages):
        if pageNum >= (i * k) + 1 and pageNum <= min((i + 1) * k, chapter):
            cnt += 1
        pageNum += 1
print(cnt)