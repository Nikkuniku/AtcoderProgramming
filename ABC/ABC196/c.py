n=int(input())

i = 1
s=int(str(i)+str(i))
ans=0
while s<=n:
    if s<=n:
        ans+=1

    i+=1
    s=int(str(i)+str(i))

print(ans)