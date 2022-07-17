n = int(input())
R = list(map(int, input().split()))
L = list(map(int, input().split()))
q = int(input())
ans = []
for _ in range(q):
    r, c = map(int, input().split())
    r, c = r-1, c-1
    p = R[r]
    if L[c] >= n-p+1:
        ans.append('#')
    else:
        ans.append('.')
print(*ans, sep="")
