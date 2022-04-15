n,q=map(int,input().split())
init=0
k=1
while n>k:
    k*=2
n=k
node=[init]*(2*k)
def update(i,x):
    i+=k-1
    node[i]+=x
    while i>1:
        i//=2
        node[i]=node[2*i]+node[2*i + 1]

def find(a,b,k=1,l=1,r=-1):
    # 要求区間[a,b)
    # 対象区間[l,r)
    if r<0:r=n+1
    # 要求区間と対象区間が交わらない
    if r<=a or b<=l:return init

    # 要求区間が対象区間を被覆している
    if a<=l and r<=b:return node[k]

    # 要求区間が対象区間の一部を被覆
    vl = find(a,b,2*k,l,(l+r)//2)
    vr = find(a,b,2*k + 1,(l+r)//2,r)
    return vl+vr
ans=[]
for _ in range(q):
    com,x,y=map(int,input().split())
    if com==0:
        update(x,y)
    else:
        ans.append(find(x,y+1))
print(node)
print(*ans,sep="\n")