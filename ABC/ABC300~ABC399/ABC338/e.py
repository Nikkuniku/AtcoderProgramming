N = int(input())
B = []
for i in range(N):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    B.append((a, i, 0))
    B.append((b, i, 1))
B.sort()
q = list()
ans = "No"
for _, i, k in B:
    if k == 1:
        j, m = q[-1]
        if i == j:
            q.pop()
        else:
            ans = "Yes"
    else:
        q.append((i, k))
print(ans)
