n=int(input())

ans=1
for a in range(1,n):
    for b in range(a+1,n):
        c=n-(a+b)
        if a**2 + b**2 ==c**2:
            ans*=(a*b*c)
        else:
            continue


print(ans)