N, M = map(int, input().split())
A = list(map(int, input().split()))


def solve(P):
    res = 0
    for i in range(N):
        tmp = []
        for j in range(i, N):
            tmp.append(P[j])
            res += sum(tmp) % M
        print(tmp)
        print(res)
    return res


print(solve(A))
