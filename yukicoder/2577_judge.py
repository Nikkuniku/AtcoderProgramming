def judge(p, q):
    if q <= p:
        return 1
    else:
        return 0


def gen(n):
    from random import shuffle

    P = [i + 1 for i in range(n)]
    shuffle(P)
    return P


def limit(n):
    from math import log2, floor

    return floor(floor((n - 1) * log2(n)) - ((n - 1) / 2) + 1)


from random import randint

for _ in range(1000):
    # N = randint(1, 100)
    N = 6
    lim = limit(N)
    P = [2, 5, 3, 4, 6, 1]
    seen = set()
    ans = []
    cnt = 0
    for i in range(N):
        s = []
        for j in range(1, N + 1):
            if j in seen:
                continue
            s.append(j)
        l = 0
        r = len(s)
        while r - l > 1:
            mid = (l + r) // 2
            Q = ans[:]
            Q.append(s[mid])
            for m in s:
                if m != s[mid]:
                    Q.append(m)
            cnt += 1
            print("?", *Q, flush=True, end="\n")
            ret = judge(P, Q)
            if ret == 1:
                l = mid
            else:
                r = mid
        ans.append(s[l])
        seen.add(s[l])
    print("!", *ans, end="\n", flush=True)
    if cnt > lim:
        print(P, cnt, lim)
        break
