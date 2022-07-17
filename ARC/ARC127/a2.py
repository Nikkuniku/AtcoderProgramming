from itertools import groupby

n = int(input())


def solve():
    cnt = [0]*20
    for k in range(1, len(str(n))+1):
        v = [0]*k
        for i in range(k):
            s = list('1'*(i+1)+'0'*(k-i-1))
            p = list('1'*(i+1)+'0'*(k-i-1))
            p[i] = '2'
            p = int(''.join(p))
            s = int(''.join(s))
            if n < p:
                if s <= n:
                    value = n-s+1
                else:
                    value = 0
            else:
                value = p-s
            v[i] = value
            if i > 0:
                v[i-1] -= value

        for i in range(k):
            cnt[i] += v[i]
    ans = 0
    for v in range(20):
        ans += cnt[v]*(v+1)
    return ans


print(solve())
