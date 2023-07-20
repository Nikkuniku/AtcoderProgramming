N, M = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
MOD = 10**9 + 7
S = ((max(X)-min(X))*(max(Y)-min(Y))) % MOD
S *= (N-2)*(M-2)
S %= MOD
print(S)
