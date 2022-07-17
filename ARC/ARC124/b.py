from itertools import permutations


def genrandomsequence(n, a, b):
    import random
    re = []
    for i in range(n):
        re.append(random.randint(a, b))
    return re


n = int(input())
for _ in range(1000):
    # a = list(map(int, input().split()))
    # b = list(map(int, input().split()))
    a = genrandomsequence(n, 0, 50)
    b = genrandomsequence(n, 0, 50)
    xor_a = 0
    xor_b = 0

    for i in range(n):
        xor_a ^= a[i]
        xor_b ^= b[i]
    p1 = permutations(a)
    p2 = permutations(b)

    ans = []
    for c in p1:
        for d in p2:
            s = set()
            for i in range(n):
                s.add(c[i] ^ d[i])

            if len(s) == 1:
                ans.append(min(s))
    if ans:
        print(*a)
        print(*b)
        print(*ans)
        print(xor_a ^ xor_b)
