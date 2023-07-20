for i in range(2, 30):
    N = i
    # N, K = map(int, input().split())
    A = [i+1 for i in range(N)]

    def shuffle(L, R):
        if L+1 == R:
            A[L-1], A[R-1] = A[R-1], A[L-1]
        else:
            shuffle(L, R-1)
            shuffle(L+1, R)
    shuffle(1, N)
    print(*A)
