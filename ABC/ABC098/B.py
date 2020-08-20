n=int(input())
s=list(input())

ans=0
for i in range(1,n):
    be=s[:i]
    af=s[i:]

    tmp = len(set(be)&set(af))
    ans=max(ans,tmp)

print(ans)
