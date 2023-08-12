N = int(input())
S = [-1]+list(input().split())
A = []
tmp = 0
for i in range(1, N+1):
    if S[i] != S[i-1]:
        tmp += 1
    else:
        A.append(tmp)
        tmp = 1
A.append(tmp)
ans=0
for i in range(len(A)):
    tmp=0
    for j in [-1,0,1]:
        if 0<=i+j<len(A):
            tmp+=A[i+j]
    ans=max(ans,tmp)
print(ans)

            