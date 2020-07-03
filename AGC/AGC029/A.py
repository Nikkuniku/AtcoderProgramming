s=input()

cnt=0
ans=0

for i in range(len(s)):
    if s[i]=='W':
        ans+=i-cnt
        cnt+=1

print(ans)