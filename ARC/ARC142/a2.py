n = int(input())


def solve(k):
    s = set()
    for i in range(1, n):
        j = i
        if i <= n:
            tmp = 10**18
            for _ in range(100):
                i = list(str(i))[::-1]
                i = ''.join(i)
                i = int(i)
                if tmp > i:
                    tmp = i
            if i == k:
                s.add(j)
    return s


print(solve(6316))
