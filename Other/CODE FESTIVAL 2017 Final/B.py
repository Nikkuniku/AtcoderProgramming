s=input()

from collections import Counter

c =dict(Counter(s))

if len(c)==1 and c[s[0]]>1:
    print('NO')
    exit(0)

if len(c)==2 and sum(list(c.values()))>2:
    print('NO')
    exit(0)

under_value = 10**18

#出現回数の最小値を探す
for _,Value in c.items():
    under_value = min(under_value,Value)
#それぞれの出現回数から引く（セット分）
for key,_ in c.items():
    c[key]-=under_value
    
f = 0
flg=0
for i,j in c.items():
    if j!=0:
        flg+=1
    f+=j
ans='YES'
if len(c)==3 and f>=3 and flg==2:
    ans='NO'
elif len(c)==3 and f>=2 and flg==1:
    ans='NO'
print(ans)


