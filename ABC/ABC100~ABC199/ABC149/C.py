X=int(input())


while True:

    flg = 0
    for i in range(1,X+1):
        if X%i==0:
            if i!=1 and  i!=X:
                flg=1
    
    if flg == 0:
        break

    X+=1

print(X)