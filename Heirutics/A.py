d=int(input())
c=list(map(int,input().split()))
s=[]
for _ in range(d):
    s_i=list(map(int,input().split()))
    s.append(s_i)

dp=[0]*26

from random import randint

def score_ans(s,c,now):
    tmp=0
    for i in range(26):
        tmp+=c[i]*(now - dp[i])
    
    return s-tmp

for i in range(d):

    score=0
    ans=s[i].index(max(s[i]))

    for j in range(26):

        s_i=s[i][j]

        if score<score_ans(s_i,c,i):
            ans=j+1
            score+=score_ans(s_i,c,i)

    dp[ans-1]=i    
    

    print(ans)