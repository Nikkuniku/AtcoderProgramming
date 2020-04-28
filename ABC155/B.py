N=int(input())
Papers = list(map(int,input().split()))

evens = [i for i in Papers if i %2==0]

flg = 0

for j in evens:
    if j%3==0 or j%5==0:
        flg += 0
    else:
        flg+=1

if flg!=0:
    print('DENIED')
else:
    print('APPROVED')