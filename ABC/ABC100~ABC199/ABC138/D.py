N,Q=map(int,input().split())

tree={}
tree[1]=-1
for n in range(2,N):
    tree[n]=1
    
cnt=[0]*N

for i in range(N-1):
    a,b = map(int,input().split())
    tree[b]=a

for j in range(Q):
    p,x=map(int,input().split())
    p-=1
    cnt[p]+=x

for k in range(1,N):
    cnt[k]+=cnt[tree[k+1]-1]

# def search(root,x):
#     leaf =[]
#     for i,j in tree.items():
#         if j ==root:
#             leaf.append(i)
        
#     if len(leaf)!=0:
#         for k in leaf:
#             search(k,x)
#             cnt[k-1]+=x

# for i in range(N-1):
#     a,b = map(int,input().split())
#     tree[b]=a
# for j in range(Q):
#     p,x=map(int,input().split())
#     if p==1:
#         cnt+=x
#     else:
#         cnt[p-1]+=x
#         search(p,x)


print(*cnt)



