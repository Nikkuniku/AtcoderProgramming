x,k,d=map(int,input().split())


if d>=abs(x):
    if k%2==0:
        p=abs(x)
    else:
        if x>=0:
            p=abs(x-d)
        else:
            p=abs(x+d)
    print(p)
    exit(0)
else:
    cnt=abs(x)//d

    if cnt>=k:
        cnt=k

    if x>=0:
        p=x-d*cnt
    else:
        p=x+d*cnt

    k-=cnt

    if k==0:
        print(abs(p))
        exit(0)

    if k%2==0:
        print(abs(p))
    else:
        if p>=0:
            p=abs(p-d)
        else:
            p=abs(p+d)

        print(p)