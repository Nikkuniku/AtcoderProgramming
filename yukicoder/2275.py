N = int(input())
A = list(map(int, input().split()))
MOD = 998244353
v = 1
for i in range(N-1):
    if i == 0:
        v = min(A[i], A[i+1])
        h = A[i+1]
        continue
    if h <= A[i+1]:
        v *= h
    else:
        h = A[i+1]
        v *= h
    v %= MOD
print(v)
