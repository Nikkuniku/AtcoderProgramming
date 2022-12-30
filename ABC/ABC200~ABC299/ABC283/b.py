N = int(input())
A = list(map(int, input().split()))
Q = int(input())
ans = []
for _ in range(Q):
    query = list(map(int, input().split()))
    q = query[0]
    if q == 1:
        k, x = query[1:]
        k -= 1
        A[k] = x
    else:
        k = query[1]-1
        ans.append(A[k])
print(*ans, sep="\n")
