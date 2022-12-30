Anntena=[]
for _ in range(5):
    Anntena.append(int(input()))

k = int(input())

from itertools import combinations

c = list(combinations(Anntena,2))

flg=0
for a in c:
    dist = abs(a[1] - a[0])

    if dist>k:
        flg+=1

if flg==0:
    print('Yay!')
else:
    print(':(') 