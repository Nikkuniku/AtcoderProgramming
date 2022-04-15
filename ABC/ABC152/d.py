n=int(input())
def solve(n,a,b):
    re=0
    # 1桁
    if a==b:
        if a<=n:re+=1
    # 2桁
    p=b*10 + a
    if p<=n:
        re+=1

    #k桁
    for k in range(3,7):
        q=min(n,(b+1)*pow(10,k-1))
        p=b*pow(10,k-1)+a
        r=(q-p)
        if r>=0:
            re += r//10 +1
    return re


ans=0
for i in range(1,n+1):
    if i%10==0:
        continue
    else:
        s=str(i)
        a=int(s[0])
        b=int(s[-1])

        ans+=solve(n,a,b)

print(ans)