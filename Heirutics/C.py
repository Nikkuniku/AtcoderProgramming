d=int(input())
c=list(map(int,input().split()))
s=[]
for _ in range(d):
    s_i=list(map(int,input().split()))
    s.append(s_i)
t=[]
for _ in range(d):
    t_i=int(input())
    t.append(t_i)

dp=[0]*26
ans=0
score=[]

for i in range(d):
    s_i = s[i][t[i]-1]
    ans+=s_i
    dp[t[i]-1]=i+1
    tmp=0
    for j in range(26):
        tmp+=c[j]*((i+1)-dp[j])

    
    

    ans -= tmp
    score.append(ans)
    print(ans)


m=int(input())
for i in range(m):
    pre,aft = map(int,input().split())
    if i==0:
        scr=score[i]
    else:
        scr=score[i-1]
    
    for j in range(pre,d):
        score[j]+=s[i][aft-1]-s[i][pre-1]-c[pre-1]*(i+1 - dp[pre-1]) - c[aft-1]*(i+1 - dp[aft-1])

    print(score[i])