x,k,d=map(int,input().split())

x=abs(x)
cnt=abs(x)//d


if cnt>=k:
    print(x-d*k)
else:
    k-=cnt

    if k%2==0:
        print(abs(x-d*cnt))
    else:
        print(abs(x-d*(cnt+1)))

