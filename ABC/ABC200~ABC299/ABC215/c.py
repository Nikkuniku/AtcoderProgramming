import itertools
s,k=input().split()

p=list(itertools.permutations(s))
ans=set()

for c in p:
    tmp=''.join(list(c))
    ans.add(tmp)
ans=sorted(list(ans))
print(ans[int(k)-1])