S = input()
N = len(S)
Q = int(input())
d = {'A': 'BC', 'B': 'CA', 'C': 'AB'}
alphabet = ['A', 'B', 'C']


def start_S(t, k):
    if t > 60:
        return 0
    return (k-1)//pow(2, t)


def idx_t(t, k):
    if t > 60:
        return k-1
    res = k-1 - start_S(t, k)*pow(2, t)
    return res


def solve(p, idx, t):
    roop = (max(t, 60)-60) % 3
    t = min(60, t)
    s = pow(2, t)-1+idx
    ope = [s]
    while s > 0:
        s -= 1
        s //= 2
        ope.append(s)
    ope = ope[::-1]
    alp = S[p]
    if len(ope) == 1:
        return alp
    for i in range(len(ope)):
        if i == 0:
            pre = ope[i]
            continue
        if 2*(pre+1) == ope[i]:
            alp = d[alp][1]
        else:
            alp = d[alp][0]
        pre = ope[i]
    alp_idx = (alphabet.index(alp)+roop) % 3
    return alphabet[alp_idx]


ans = []
for _ in range(Q):
    t, k = map(int, input().split())
    p = start_S(t, k)
    idx = idx_t(t, k)
    ans.append(solve(p, idx, t))
print(*ans, sep="\n")
