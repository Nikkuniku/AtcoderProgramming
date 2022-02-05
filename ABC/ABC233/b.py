l,r=map(int,input().split())
s=list(input())

s_l=[]
s_mid=[]
s_r=[]

for i in range(len(s)):
    if i+1<l:
        s_l.append(s[i])
    elif l<=i+1<=r:
        s_mid.append(s[i])
    elif r<i+1:
        s_r.append(s[i])

s_mid=list(reversed(s_mid))

ans=''.join(s_l+s_mid+s_r)
print(ans)