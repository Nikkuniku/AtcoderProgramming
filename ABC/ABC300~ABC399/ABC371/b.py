from collections import defaultdict

N, M = map(int, input().split())
Male = defaultdict(int)
ans = []
for _ in range(M):
    a, b = input().split()
    if b == "M":
        if Male[a] == 0:
            ans.append("Yes")
            Male[a] += 1
            continue
    ans.append("No")
print(*ans, sep="\n")
