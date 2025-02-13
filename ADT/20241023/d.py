N, M = map(int, input().split())
male = [0] * N
ans = []
for _ in range(M):
    a, b = input().split()
    a = int(a)
    res = "No"
    if b == "M":
        if male[a - 1] == 0:
            res = "Yes"
        male[a - 1] += 1
    ans.append(res)
print(*ans, sep="\n")
