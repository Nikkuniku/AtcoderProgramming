s=input().split('+')



if len(s)==1:
    ans=1
    for j in range(len(s[0])):
        if s[0][j]!='*':
            ans*=int(s[0][j])
    if ans!=0:
        ans=1
    else:
        ans=0
    print(ans)
    exit(0)

ans=0
for i in range(len(s)):
    if eval(s[i])==0:
        continue
    ans+=1
 
print(ans)