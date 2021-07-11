from sys import stdin

n=int(input())
s=list(input())
q=int(input())

shift=0

for _ in range(q):
    t,a,b=map(int, stdin.readline().split())
    
    if t==1:
        a,b=a-1,b-1
        s[(a+shift)%(2*n)],s[(b+shift)%(2*n)] = s[(b+shift)%(2*n)],s[(a+shift)%(2*n)]
    elif t==2:
        shift=(shift+n)%(2*n)

if shift%(2*n)==0:
    ans=''.join(s)
else:
    ans=''.join(s[n:]+s[:n])

print(ans)