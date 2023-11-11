N, L = map(int, input().split())
A = list(map(int, input().split()))
idx = -1
for i in range(N):
    if A[i] == 2:
        idx = i
csum = 0
for i in range(idx):
    csum += A[i]+1

if L-csum >= 2:
    print('Yes')
else:
    print('No')
