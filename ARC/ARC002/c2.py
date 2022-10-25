n=int(input())
s=input()
command=['AA','AB','AX','AY','BA','BB','BX','BY','XA','XB','XX','XY','YA','YB','YX','YY']
INF=1<<18
ans=[]
for L in command:
    for R in command:
        if L==R:
            continue
        shortcut=set([L,R])
        dp=[INF]*(n+1)
        dp[0]=0
        for i in range(n):
            dp[i+1]=min(dp[i+1],dp[i]+1)
            if i>0 and s[i-1:i+1] in shortcut:
                dp[i+1]=min(dp[i+1],dp[i-1]+1)
        ans.append(dp[n])
print(min(ans))

        