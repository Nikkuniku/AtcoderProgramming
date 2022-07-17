def solve(n):
    n = str(n)
    L = len(n)
    re = [int('9'*(L-1))]
    res = 0
    for i in range(1, L):
        if L % i == 0:
            z = n[:i]
            p = int(z*(L//i))
            if p <= int(n):
                res = p
            else:
                res = str(int(z)-1)*(L//i)
            re.append(int(res))
    return max(re)


t = int(input())
ans = []
for _ in range(t):
    c = input()
    ans.append(solve(c))
print(*ans, sep="\n")
