n=int(input())
a=list(map(int,input().split()))

if a.count(0)>0:
    print(0)
    exit(0)

total=1
for i in a:
    total *=i

    if total>10**18:
        print(-1)
        exit(0)
    
print(total)