T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    tmp = 0
    for a in A:
        if a % 2 != 0:
            tmp += 1
    ans.append(tmp)
print(*ans, sep="\n")
