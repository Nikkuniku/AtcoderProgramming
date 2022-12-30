import datetime
H, M = map(int, input().split())

a = datetime.datetime(100, 1, 1, H, M, 0)
for i in range(2000):
    b = a + datetime.timedelta(minutes=i)
    AB = ('0'+str(b.hour))[-2:]
    CD = ('0'+str(b.minute))[-2:]
    Hour = int(AB[0]+CD[0])
    Minutes = int(AB[1]+CD[1])
    if Hour <= 23 and Minutes <= 59:
        print(AB, CD)
        break
