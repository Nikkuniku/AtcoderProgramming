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
for i in range(d):
    s_i = s[i][t[i]-1]
    ans+=s_i
    dp[t[i]-1]=i+1
    tmp=0
    for j in range(26):
        tmp+=c[j]*((i+1)-dp[j])

    
    

    ans -= tmp

    print(ans)