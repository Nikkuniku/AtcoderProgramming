s=input()
n=len(s)

if s=='zyxwvutsrqponmlkjihgfedcba':
    print(-1)
    exit(0)


from collections import Counter

t="abcdefghijklmnopqrstuvwxyz"
d={}
dp={}
for i in range(len(t)):
    d[t[i]]=i
    dp[i]=t[i]

ans=[]

for j in range(n):
    ans.append(d[s[j]])

if len(ans)<26:
    for k in range(27):
        if k not in ans:
            ans.append(k)
            break


    s_str=''
    for l in range(len(ans)):
        s_str+=dp[ans[l]]

    print(s_str)
else:
    flg=1
    can=[]
    for k in range(len(ans)-1):
        if ans[k]>ans[k+1]:
            index=k
        else:
            can=[]
    if ans[24]>ans[25]
