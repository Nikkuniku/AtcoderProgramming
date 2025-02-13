T = int(input())
ans = []
for _ in range(T):
    a, s = map(int, input().split())
    res = "No"
    if (s - 2 * a) >= 0 and (s - 2 * a) & a == 0:
        res = "Yes"
    ans.append(res)
print(*ans, sep="\n")
