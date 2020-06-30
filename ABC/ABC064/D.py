n=int(input())
s=input()

d=[0]*n

cnt=0
for i in range(n):
    if s[i]=='(':
        cnt+=1
    else:
        cnt-=1
    d[i]=cnt

x=min(d)

s='('*(-x) + s

d2=[0]*(len(s))
cnt=0
for i in range(len(s)):
    if s[i]=='(':
        cnt+=1
    else:
        cnt-=1
    d2[i]=cnt

s=s+')'*d2[-1]

print(s)