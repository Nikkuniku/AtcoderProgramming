N, L = map(int, input().split())
A = list(map(int, input().split()))
k = -1
for i in range(N):
    if A[i] == 2:
        k = i
if k == -1:
    print('Yes')
    exit()

tmp = sum(A[:k])+k
ans = 'No'
if L-tmp >= 2:
    ans = 'Yes'
print(ans)
