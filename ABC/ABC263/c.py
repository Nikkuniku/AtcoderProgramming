from itertools import permutations
n, m = map(int, input().split())
num = [i for i in range(1, m+1)]


per = permutations(num, n)

ans = []
for p in per:
    q = sorted(list(p))
    if list(p) == q:
        ans.append(q)
ans.sort()
for a in ans:
    print(*a)
