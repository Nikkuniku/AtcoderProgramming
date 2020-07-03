n,k=map(int,input().split())
a=list(map(int,input().split()))

from collections import Counter

c=Counter(a).most_common()[:k]
cnt=0
for i in c:
    cnt+=i[1]

print(n-cnt)

# s=set([i[0] for i in c])

# ans=0
# for i in range(n):
#     if a[i] not in s:
#         ans+=1

# print(ans)

