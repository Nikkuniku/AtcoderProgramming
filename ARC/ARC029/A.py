n=int(input())
meet=[]
for _ in range(n):
    meet.append(int(input()))

from itertools import combinations

ans=0
if n<=2:
    ans = max(meet)
elif n==3:
    p=combinations(meet,2)
    ans=10**9
    for c in p:
        s_1 = sum(c)
        s_2 = sum(meet)-s_1

        ans = min(ans,max(s_1,s_2))

elif n==4:
    p=combinations(meet,2)
    ans=10**9
    for c in p:
        s_1 = sum(c)
        s_2 = sum(meet)-s_1

        ans = min(ans,max(s_1,s_2))
    
    p=combinations(meet,3)
    for c in p:
        s_1 = sum(c)
        s_2 = sum(meet)-s_1

        ans = min(ans,max(s_1,s_2))

    
print(ans)