a=list(map(int,input().split()))
import itertools
p=list(itertools.permutations(a))

ans='No'
for b in p:
    if b[1]-b[0]==b[2]-b[1]:
        ans='Yes'
        break

print(ans)