n= int(input())
from itertools import combinations
d=[0,0,0,0,0]

f={}
f['M']=0
f['A']=1
f['R']=2
f['C']=3
f['H']=4

e={}
e['M']=0
e['A']=0
e['R']=0
e['C']=0
e['H']=0


for _ in range(n):

    s = input()[0]
    if s in ['M','A','R','C','H']:
        e[s]=1
        d[f[s]]+=1


k = e['M']+e['A']+e['R']+e['C']+e['H']

cnt=0
if k>=3:
    c = list(combinations(d,3))

    for j in c:
        tmp=1
        for l in j:
            tmp*=l
        
        cnt+=tmp

print(cnt)
