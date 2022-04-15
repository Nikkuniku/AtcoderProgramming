s=list(input())
k=int(input())
n=len(s)
def diff(s):
    re=ord('z')-ord(s)+1
    if s=='a':
        re=0
    return re
def al(s,m):
    q=97+(ord(s)-97+m)%26
    return chr(q)

p=[]
for i in range(n):
    p.append(diff(s[i]))
ans=[]
for i in range(n-1):
    c=s[i]
    if c!='a':
        if p[i]<=k:
            c=al(s[i],p[i])
            k-=p[i]
    ans.append(c)
ans.append(al(s[-1],k))
print(''.join(ans))