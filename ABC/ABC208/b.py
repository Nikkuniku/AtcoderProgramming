p=int(input())
coin=[]
from math import copysign, factorial
for i in range(1,11):
    coin.append(factorial(i))
coin=sorted(coin,reverse=True)
i=0
ans=0
while True:
    cnt=p//coin[i]
    ans+=cnt
    p-=coin[i]*cnt
    if p==0:
        break
    i+=1
print(ans)
