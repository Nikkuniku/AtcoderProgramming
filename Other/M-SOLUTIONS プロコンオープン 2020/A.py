x=int(input())

if 400<=x and x<=599:
    ans=8
elif 600<= x and x<=799:
    ans=7
elif 800<= x and x<=999:
    ans=6
elif 1000<= x and x<=1199:
    ans=5
elif 1200<= x and x<=1399:
    ans=4
elif 1400<= x and x<=1599:
    ans=3
elif 1600<= x and x<=1799:
    ans=2
else:
    ans=1

print(ans)