from string import ascii_uppercase
d=dict()
e=dict()
for j in range(10):
    d[j]=ascii_uppercase[j]
    d[ascii_uppercase[j]]=j
N=int(input())
S=input()
MOD=998244353
dp=[[[0]*10 for _ in range(1<<10)] for _ in range(N+1)]

for i in range(N):
    t=S[i]
    p=e[S[i]]
    for s in range(1<<10):
        if s&(1<<p):
            for j in range(10):    
                dp[i+1][s][p]+=dp[i][s][p]
                dp[i+1][s][p]%=