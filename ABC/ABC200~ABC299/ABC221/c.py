n=input()
ans=0
from itertools import permutations
for i in range(1,1<<len(n)-1):
    a=[]
    b=[]
    for j in range(len(n)):
        if (i>>j)&1:
            a.append(n[j])
        else:
            b.append(n[j])
        
    p=list(permutations(a))
    q=list(permutations(b))

    for k in p:
        for m in q:
            num1=''.join(k)
            num2=''.join(m)

            ans=max(ans,int(num1)*int(num2))
print(ans)