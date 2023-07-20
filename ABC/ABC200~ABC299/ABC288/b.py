N, K = map(int, input().split())
S = [input() for _ in range(N)]
S = S[:K]
print(*sorted(S), sep="\n")
