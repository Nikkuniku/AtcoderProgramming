from itertools import accumulate
N = int(input())
S = list(input())
A = [0]
B = [0]
for i in range(N):
    if S[i].isdigit():
        A.append(A[-1])
        B.append(B[-1]+1)
    else:
        A.append(A[-1]+1)
        B.append(B[-1])
ans = 1 << 60
for i in range(N+1):
    tmp = (A[-1]-A[i])+B[i]
    ans = min(ans, tmp)
print(ans)
