N, M = map(int, input().split())
baby = [0] * N
ans = []
for _ in range(M):
    a, b = input().split()
    res = "No"
    if b == "M":
        if baby[int(a) - 1] == 0:
            res = "Yes"
            baby[int(a) - 1] += 1
    ans.append(res)
print(*ans, sep="\n")
