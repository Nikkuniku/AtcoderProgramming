k,a,b=map(int,input().split())


bisket=1

cnt=a-bisket

if cnt>k:
    print(1+k)
    exit(0)

k-=cnt
bisket+=cnt

if a+2<=b:
    trade=k//2
    k-=trade*2
    
    bisket+=trade*(b-a)

    if k==1:
        bisket+=1
    
    print(bisket)


else:
    print(bisket+k)