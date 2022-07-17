from itertools import groupby

for p in range(1, 100):
    n = p

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
                    value = n-s+1
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
        print(ans)

    def solve2():
        cnt = [0]*20
        for i in range(n+1):
            s = str(i)
            j = 0
            while j < len(s):
                if s[j] == '1':
                    pass
                else:
                    break
                j += 1
            cnt[j] += 1
        ans = 0
        for v in range(20):
            ans += cnt[v]*(v)
        print(ans)

    print(p)
    solve()
    solve2()
    print('--')
