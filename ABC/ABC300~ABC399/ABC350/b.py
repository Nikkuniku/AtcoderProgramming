N, Q = map(int, input().split())
T = [True] * N
A = list(map(int, input().split()))
for i in range(Q):
    t = A[i] - 1
    if T[t]:
        T[t] = False
    else:
        T[t] = True
print(sum(T))
