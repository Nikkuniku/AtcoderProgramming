N, K, L = map(int, input().split())

from itertools import product, combinations


def make(N, K, L):
    S = [str(i) for i in range(L)]
    P = list(product(S, repeat=N))
    C = list(combinations(range(N), K))
    ans = []
    for a in P:
        seen = set()
        isOK = True
        for c in C:
            tmp_str = "".join([a[k] for k in c])
            if tmp_str in seen:
                isOK = False
                break
            seen.add(tmp_str)
        if isOK:
            ans.append("".join(a))
    print(len(ans))
    # print(*ans, sep="\n")


for k in range(1, L + 1):
    make(N, K, k)
# make(N, K, L)
