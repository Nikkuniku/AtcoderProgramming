a,b,c=map(int,input().split())

ans='No'

if c>1:
    k=1
    while True:
        if a<pow(c,k):
            break
        else:
            k+=1

    if b>=k:
        ans='Yes'
print(ans)
