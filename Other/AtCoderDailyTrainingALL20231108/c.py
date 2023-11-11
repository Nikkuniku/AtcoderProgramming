N = int(input())
S = set([i for i in range(N + 1)])
A = list(map(int, input().split()))
for a in A:
    S.discard(a)
print(min(S))
