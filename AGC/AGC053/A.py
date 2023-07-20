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


def judge(a, b, s):
    c = a[:]
    res = True
    for i in range(len(c)):
        c[i] -= b[i]
        if c[i] < 0:
            return False
    for i in range(len(s)):
        if s[i] == '>':
            if not (c[i] >= c[i+1]):
                res = False
        elif s[i] == '<':
            if not (c[i] <= c[i+1]):
                res = False
    return res


N = int(input())
S = input()
A = list(map(int, input().split()))
B = Base(N, S)
ans = []
while judge(A, B, S):
    ans.append(B[:])
    for i in range(N+1):
        A[i] -= B[i]
for i in range(N+1):
    ans[0][i] += A[i]
print(len(ans))
for c in ans:
    print(*c)
