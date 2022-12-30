from sys import prefix, stdin

n=int(input())
s=list(input())
q=int(input())

pre=s[:n]
post=s[n:]

for _ in range(q):
    t,a,b=map(int, stdin.readline().split())

    if t==1:
        a,b=a-1,b-1
        if b<=n-1:
            pre[a],pre[b] = pre[b],pre[a]
        elif a>=n:
            post[a-n],post[b-n]=post[b-n],post[a-n]
        else:
            pre[a],post[b-n]=post[b-n],pre[a]
    else:
        pre,post = post,pre

ans=''.join(pre+post)
print(ans)