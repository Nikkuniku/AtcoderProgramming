N = int(input())
A = list(map(int, input().split()))
cnt = [0] * (N + 1)
ans = set([i + 1 for i in range(N)])
for a in A:
    cnt[a] += 1
    if cnt[a] == 4:
        ans.discard(a)
print(min(ans))
