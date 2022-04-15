n,k=map(int,input().split())
s=input()
INF =10**9
c=[[INF]*(26)for _ in range(n)]
def alpha2num(s):
    return ord(s)-ord('a')
def num2alpha(n):
    return chr(n+65)
for i in range(n-1,-1,-1):
    c[i][alpha2num(s[i])]=i
    if i-1>=0:
        for j in range(26):
            c[i-1][j]=c[i][j]
ans=[]
now=0
for i in range(k):
    for j in range(26):
        if c[now][j]<=n-k+i:
            ans.append(num2alpha(j).lower())
            now=c[now][j]+1
            break

print(''.join(ans))