N, K = map(int, input().split())
Snuke = set([i + 1 for i in range(N)])
for _ in range(K):
    d = int(input())
    s = list(map(int, input().split()))
    for j in s:
        Snuke.discard(j)
print(len(Snuke))
