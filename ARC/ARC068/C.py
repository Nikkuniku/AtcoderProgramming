x=int(input())

cnt=x%11

ans=2*(x//11)
if cnt>=1 and cnt<=6:
    ans+=1
elif cnt>=7 and cnt<=10:
    ans+=2

print(ans)