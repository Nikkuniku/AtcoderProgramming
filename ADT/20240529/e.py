N, M = map(int, input().split())
A = [list(input()) for _ in range(2 * N)]
B = [i for i in range(2 * N)]
W = [0] * (2 * N)
ans = []
for j in range(M):
    for i in range(N):
        p = B[2 * i]
        q = B[2 * i + 1]
        if A[p][j] == "G" and A[q][j] == "C":
            W[p] += 1
        elif A[p][j] == "C" and A[q][j] == "P":
            W[p] += 1
        elif A[p][j] == "P" and A[q][j] == "G":
            W[p] += 1
        elif A[p][j] == "C" and A[q][j] == "G":
            W[q] += 1
        elif A[p][j] == "P" and A[q][j] == "C":
            W[q] += 1
        elif A[p][j] == "G" and A[q][j] == "P":
            W[q] += 1
    C = []
    for v, win in enumerate(W):
        C.append((win, v))
    C.sort(key=lambda x: x[1])
    C.sort(key=lambda x: x[0], reverse=True)
    B = [v for _, v in C]
for p in B:
    print(p + 1)
