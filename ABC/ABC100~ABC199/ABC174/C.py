k=int(input())


if k%2==0 or k%5==0:
    print(-1)
    exit(0)

d={}

x=7
i=1
while True:
    if x%k==0:
        print(i)
        exit(0)

    x=(10*x + 7)%k
    if x not in d:
        d[x]=1
    else:
        print(-1)
        exit(0)


    i+=1
    


