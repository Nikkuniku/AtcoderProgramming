n=pow(2,20)
node=[-1]*(2*n -1)
# i番目をxに更新
def update(i,x):
    i+=n-1
    node[i]=x
    while i>1:
        i=(i-1)//2
        node[i]=min(node[2*i +1],node[2*i + 2])

# 要求区間[a,b)
# 対象区間[l,r)
# 現在のノードk
# 閾値x
def find(a,b,x):
    return find_sub(a,b,x,0,0,n)

def find_sub(a,b,x,k,l,r):
    # 対象区間外
    if node[k]>x or r<=a or b<=l:
        return a-1
    # 探索中のノードが葉
    elif k>=n-1:
        return k-(n-1)
    else:
        vl = find_sub(a,b,x,2*k +1,l,(l+r)//2)
        if vl!=a-1:
            return vl
        else:
            return find_sub(a,b,x,2*k +2,(l+r)//2,r)

q=int(input())
ans=[]
for _ in range(q):
    t,x=map(int,input().split())
    if t==1:
        p=find(x%n,n,-1)
        if p!=(x%n)-1:
            index=p
        else:
            index=find(0,x%n,-1)
        update(index,x)
    else:
        ans.append(node[(x%n)+n-1])
print(*ans,sep="\n")