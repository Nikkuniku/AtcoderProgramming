from datetime import date,timedelta

da=input().split('/')
y=int(da[0])
m=int(da[1])
d=int(da[2])

td = timedelta(days=1)

now=date(y,m,d)
while True:
    if (now.year/now.month/now.day).is_integer():
        break

    now=now+td



print(now.strftime('%Y/%m/%d'))