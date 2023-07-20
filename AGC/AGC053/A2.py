
def Base(N, S):
    N = N + 1

    A = [0] * N
    B = [0] * N

    for i in range(1, N):
        if S[i-1] == "<":
            A[i] = A[i-1] + 1
    for i in range(N-1)[::-1]:
        if S[i] == ">":
            B[i] = B[i+1] + 1

    C = [max(A[i], B[i]) for i in range(N)]
    return C


N = int(input())
S = input()
A = list(map(int, input().split()))
B = Base(N, S)
ans = []
for k in range(10001):
    C = []
    isOK = True
    for i in range(N+1):
        if A[i]-k*B[i] < 0:
            isOK = False
        C.append(A[i]-k*B[i])
    for i in range(N):
        if S[i] == '>':
            if not C[i] > C[i+1]:
                isOK = False
        elif S[i] == '<':
            if not C[i] < C[i+1]:
                isOK = False
    if isOK:
        ans = [C]+[B for _ in range(k)]
    else:
        break
print(len(ans))
for c in ans:
    print(*c)
