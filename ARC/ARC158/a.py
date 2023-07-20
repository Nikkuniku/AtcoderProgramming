def solve(pList):
    pList = sorted(pList)
    X = sum(pList)
    if X % 3 != 0:
        return -1
    res = 0
    for p in pList:
        if ((X//3)-p) % 2 != 0:
            return -1
        res = max(res, abs((X//3)-p))
    return res//2


T = int(input())
ans = []
for _ in range(T):
    case = list(map(int, input().split()))
    ans.append(solve(case))
print(*ans, sep="\n")
