N = int(input())
S = set([i + 1 for i in range(2 * N + 1)])
while 1:
    t = min(S)
    print(min(S), flush=True)
    S.discard(t)
    A = int(input())
    if A == 0:
        break
    S.discard(A)
