n=int(input())

cnt=0
for a in range(1,n+1):
    b=n//a
    c=n-a*b

    if c==0:
        cnt+=b-1
    else:
        cnt+=b


print(cnt)



