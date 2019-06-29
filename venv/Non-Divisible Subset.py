def solveSubset(S, k, n):
    r = [0] * k

    for value in S:
        r[value % k] += 1

    result = 0
    for a in range(1, (k + 1) // 2):
        result += max(r[a], r[k - a])
    if k % 2 == 0 and r[k // 2]:
        result += 1
    if r[0]:
        result += 1
    return result


nk = input().split()

n = int(nk[0])

k = int(nk[1])

S = list(map(int, input().rstrip().split()))

print(solveSubset(S, k, n))
