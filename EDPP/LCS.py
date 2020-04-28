S=input()
T=input()

s,t=len(S),len(T)
#DPテーブル作成
dp=[[0]*(t+1) for _ in range(s+1)]

for i in range(s):
    for j in range(t):
        if S[i] ==T[j]:
            dp[i+1][j+1] =dp[i][j] + 1
        else:
            dp[i+1][j+1] =  max([ dp[i+1][j] , dp[i][j+1] ])
print(*dp,sep="\n")

print(s,t)

# S[i]とT[j]が同じ時に値が更新される
# ⇒値が更新された時のi,jの組を答える
res = ''
while s != 0 and t != 0:
    if dp[s][t] == dp[s-1][t]:
        s -= 1
    elif dp[s][t] == dp[s][t-1]:
        t -= 1
    else:
        s -= 1
        t -= 1
        res = S[s] + res
        print(res)

# print(dp[s][t])
print(res)