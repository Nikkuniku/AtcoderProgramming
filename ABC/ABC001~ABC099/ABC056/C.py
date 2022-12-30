x= int(input())

if x==1:
    print(1)
    exit(0)

cnt=1
iterate=2
while cnt<x:
    cnt+=iterate

    if x<=cnt:
        break
    iterate+=1


print(iterate)


