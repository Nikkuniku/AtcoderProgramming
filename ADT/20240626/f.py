N, K = map(int, input().split())
A = list(map(int, input().split()))
B = set(A)
s = set()
for i in range(K):
    if i in B:
        s.add(i)
    else:
        break
if len(s) == 0:
    ans = 0
else:
    ans = max(s) + 1
print(ans)
