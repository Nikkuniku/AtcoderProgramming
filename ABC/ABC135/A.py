a,b=map(int,input().split())

c1= (a-b)/2
c2= (b-a)/2

if abs(a-(a-c1))==abs(b-(a-c1)) and c1.is_integer():
    print(int(a-c1))
elif abs(a-(b-c2))==abs(b-(b-c2)) and c2.is_integer():
    print(int(b-c2))
else:
    print('IMPOSSIBLE')