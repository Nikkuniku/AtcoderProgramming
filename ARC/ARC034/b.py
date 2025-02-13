def f(k):
    digits = list(map(int, list(str(k))))
    return sum(digits)


N = int(input())
ans = []
for d in range(1, min(200, N) + 1):
    tmp = N - d
    if f(tmp) == d:
        ans.append(tmp)
ans.sort()
print(len(ans))
if ans:
    print(*ans, sep="\n")
