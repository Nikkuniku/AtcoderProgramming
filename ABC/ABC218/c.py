n=int(input())
s=[list(input()) for _ in range(n)]
t=[list(input()) for _ in range(n)]

def solve(s):
    re=[]
    cln=0
    brankclomun=True
    for j in range(n):
        cnt=0
        for i in range(n):
            if s[i][j]=='#':
                cnt+=1
                re.append(n*i+j)
                brankclomun=False 
        if brankclomun and cnt==0:
            cln+=1
    a=min(re)
    div= a//n
    for j in range(len(re)):
        re[j]=re[j]-div*n-cln
    
    re.sort()
    return re

ans=solve(s)
def rotate(m):
    re=[]
    for x in zip(*m[::-1]):
       re.append(list(x))
    return(re)

answer='No'
for _ in range(4):
    p=solve(t)
    if ans==p:
        answer='Yes'
    t=rotate(t)
print(answer)