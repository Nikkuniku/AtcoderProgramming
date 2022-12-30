N,M=map(int,input().split())


numbers=[]

joken =[]

for _ in range(M):
    s,c = map(int,input().split())
    joken.append([s,c])

if N==1:
    start = 0
    end = 9
elif N==2:
    start =10
    end =99
else:
    start =100
    end =999

for i in range(start,end+1):
    
    i=str(i)

    flg =0
    for j in joken:
        if i[j[0]-1]!=str(j[1]):
            flg+=1

    if flg ==0:
        numbers.append(i)

if len(numbers)==0:
    print(-1)
else:
    print(min(numbers))



    
