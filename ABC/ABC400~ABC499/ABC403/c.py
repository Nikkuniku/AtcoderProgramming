N, M, Q = map(int, input().split())
A = [set() for _ in range(N)]
B = [False] * N
ans = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        X, Y = query[1:]
        X -= 1
        A[X].add(Y)
    elif query[0] == 2:
        X = query[1] - 1
        B[X] = True
    else:
        X, Y = query[1:]
        X -= 1
        res = "No"
        if B[X] or Y in A[X]:
            res = "Yes"
        ans.append(res)
print(*ans, sep="\n")
