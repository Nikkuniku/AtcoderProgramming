def solve(n, a, b):
    if n < a:
        return False
    if n // 2 <= a:
        if (n - a) * (n - a) < b:
            return False
    else:
        if (n - a) * ((n + 1) // 2) < b:
            return False
    return True


T = int(input())
ans = []
for _ in range(T):
    N, A, B = map(int, input().split())
    tmp = "No"
    if solve(N, A, B):
        tmp = "Yes"
    ans.append(tmp)
print(*ans, sep="\n")
