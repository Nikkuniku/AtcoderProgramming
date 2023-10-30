from sys import setrecursionlimit
from itertools import permutations
setrecursionlimit(10**8)
N=int(input())
R=list(input())
C=list(input())
p=list(permutations(range(N),3))
d={0:'A',1:'B',2:'C'}
def check(array):
    # 行について
    for i in range(len(array)):
        rcnt=0
        for j in range(N):
            if array[i][j]!='.':
                rcnt+=1
                if array[i][j]!=R[i] and rcnt==1:
                    return False
    # 列について
    for j in range(N):
        ccnt=0
        a,b,c=0,0,0
        for i in range(len(array)):
            if array[i][j]!='.':
                ccnt+=1
                if array[i][j]!=C[j] and ccnt==1:
                    return False
            a+=array[i][j]=='A'
            b+=array[i][j]=='B'
            c+=array[i][j]=='C'
        if len(array)<N and max(a,b,c)>=2:
            return False
        if len(array)==N and not ( min(a,b,c)==max(a,b,c)==1):
            return False
    return True


def dfs(arr,j):
    if j==N:
        print('Yes')
        for c in arr:
            print(*c,sep="")
        exit()
    for pi in p:
        tmp=['.']*N
        for i in range(3):
            tmp[pi[i]]=d[i]
        arr.append(tmp)
        if check(arr):
            dfs(arr,j+1)
        arr.pop()
dfs([],0)
print('No')