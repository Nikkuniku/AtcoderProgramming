
import random

# n, k = map(int, input().split())
for _ in range(100):
    n = random.randint(1, 10000)
    k = random.randint(1, 10000)

    print(n, k)

    def solve(k):
        s = set()
        for i in range(1, n+1):
            j = i
            if i <= n:
                tmp = 10**18
                for _ in range(100):
                    i = list(str(i))[::-1]
                    i = ''.join(i)
                    i = int(i)
                    if tmp > i:
                        tmp = i
                if tmp == k:
                    s.add(j)
        return len(s)

    z = solve(k)
    # print(z)

    ans = 0
    p = str(k)[0]
    q = str(k)[-1]
    if p <= q:
        # 1
        x = k
        s = set()
        for i in range(20):
            if 1 <= x <= n:
                s.add(x)
            x *= 10
        # 2
        k = ''.join(list(str(k))[::-1])
        k = int(str(k))
        x = k
        for i in range(20):
            if 1 <= x <= n:
                s.add(x)
            x *= 10
        ans = len(s)

    # print(ans)
    if z != ans:
        print('error')
