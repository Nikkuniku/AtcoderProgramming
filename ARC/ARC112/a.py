t = int(input())


def solve(a, b):
    if 2*a > b:
        return 0
    p = (b-a+1)*(b - 3*a + 2)//2
    q = a*(a-1)//2
    return p+q


ans = []
for _ in range(t):
    l, r = map(int, input().split())
    ans.append(solve(l, r))
print(*ans, sep="\n")
