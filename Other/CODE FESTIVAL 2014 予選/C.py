a,b = map(int,input().split())

if a%4==0:
    n_4 = (b//4) - (a//4) +1
else:
    n_4 = (b//4) - (a//4) 

if a%100==0:
    n_100 = (b//100) - (a//100) +1
else:
    n_100 = (b//100) - (a//100)


if a%400==0:
    n_400 = (b//400) - (a//400) +1
else:
    n_400 = (b//400) - (a//400)


print(n_4 - n_100 + n_400)
