N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))
exit = False
for i in range(N):
    if C[i] == T:
        exit = True
if not exit:
    T = C[0]
res = []
for i in range(N):
    if C[i] == T:
        res.append((R[i], i+1))
res.sort(key=lambda x: x[0], reverse=True)
ans = res[0][1]
print(ans)
