def is_prime(i):
    if i <= 1:
        return False
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            return False
    return True


def ischeck(B):
    dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(N):
        for j in range(N):
            for dx, dy in dxy:
                ni = i + dx
                nj = j + dy
                if not (0 <= ni < N and 0 <= nj < N):
                    continue
                if is_prime(B[i][j] + B[ni][nj]):
                    return False
    return True


from itertools import permutations

N = int(input())
P = permutations([i for i in range(N * N)])
for p in P:
    A = [[-1] * N for _ in range(N)]
    for i, v in enumerate(p):
        A[v // N][v % N] = i + 1
    if ischeck(A):
        print("-------")
        for c in A:
            print(*c, sep="")
        print("-------")
