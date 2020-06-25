k,t=map(int,input().split())
a=list(map(int,input().split()))

ans=max(max(a)-1 - (k-max(a)),0)
print(ans)
# from collections import deque
# d={}
# numbers=deque([])
# for i in range(t):
#     d[i+1]=a[i]

# d=sorted(d.items(),key=lambda x: x[1],reverse=True)

# c=[]
# for i in range(t):
#     c.append([d[i][0],d[i][1]])

# cnt=0
# i=0
# seq=[]
# while cnt<t:
#     if c[i][1]>0:
#         seq.append(c[i][0])
#         c[i][1]-=1
#         if c[i][1]==0:
#             cnt+=1
        
#     tmp=[j[1] for j in seq]
#     index=tmp.index(max(tmp))
#     if i!=index:
#         i=index
#     else:
#         i+=1
#     if i==t:
#         i=0


# for k in range(len(numbers)):
#     if k%2==0:
#         b=numbers.popleft()
#     else:
#         b=numbers.pop()
#     seq.append(b)

# from itertools import groupby
# length=0
# for key, group in groupby(seq):
#     length=max(length, len(list(group)))

# print(seq)
# print(length-1)