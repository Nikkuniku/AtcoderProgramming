N, M = map(int, input().split())
A = list(map(int, input().split()))


def IsOK(m, a):
    s = set()
    for v in a:
        s.add(v)
    return len(s) == m


ans = 0
while IsOK(M, A):
    ans += 1
    A.pop()
print(ans)
