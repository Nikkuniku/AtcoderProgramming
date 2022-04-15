N,m=map(int,input().split())
a=list(map(int,input().split()))
INF=10**8
init=INF
from collections import deque ,defaultdict
n=1
N+=1
while N>n:
    n*=2
node=[init]*(2*n -1)
def update(i,x):
    i+=n-1
    node[i]=x
    while i>0:
        i=(i-1)//2
        node[i]=min(node[2*i +1],node[2*i + 2])

def find(a,b,k=0,l=0,r=-1):
    # 要求区間[a,b)
    # 対象区間[l,r)
    if r<0:r=N
    # 要求区間と対象区間が交わらない
    if r<=a or b<=l:return init

    # 要求区間が対象区間を被覆している
    if a<=l and r<=b:return node[k]

    # 要求区間が対象区間の一部を被覆
    vl = find(a,b,2*k + 1,l,(l+r)//2)
    vr = find(a,b,2*k + 2,(l+r)//2,r)
    return vl+vr

for i in range(N):
    update(i,i)
d=defaultdict(int)
q=deque([])
mexes=[]
for j in range(N-1):
    v=a[j]
    q.append(v)
    d[v]+=1
    update(v,INF)
    if len(q)>m:
        w=q.popleft()
        d[w]-=1
        if d[w]==0:
            update(w,w)
    if len(q)==m:
        mexes.append(find(0,N))
ans=min(mexes)
print(ans)