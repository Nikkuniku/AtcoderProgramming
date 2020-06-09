N=int(input())
lenga=list(map(int,input().split()))

cnt =0
index =1
i=0
while i <N:
    if lenga[i]!=index:
        cnt+=1
    else:
        index+=1

    i+=1

if cnt>N-1:
    print('-1')
else:
    print(cnt)