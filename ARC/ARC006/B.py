n,l=map(int,input().split())
amida=[]


for _ in range(l):
    amida.append(list(input()))
go=list(input())

if n==1:
    print(1)
    exit(0)
    
ans=0

for i in range(2*n - 1):
    if i%2==1:
        continue

    d=0
    start=i
    visited=[[0]*(2*n) for i in range(l)]
    visited[d][i]=1
    while d<l:
        if i==0:
            if amida[d][i+1]=='-' and visited[d][i+1]==0: 
                visited[d][i+1]=1
                i+=2
            else:
                d+=1
        elif i==2*n -2 :
            if amida[d][i-1]=='-' and visited[d][i-1]==0:
                visited[d][i-1]=1
                i-=2    
            else:
                d+=1
        elif amida[d][i-1]=='-' and visited[d][i-1]==0:
            visited[d][i-1]=1
            i-=2
        elif amida[d][i+1]=='-' and visited[d][i+1]==0:
            visited[d][i+1]=1
            i+=2
        else:
            d+=1
    if go[i]=='o':
        ans=start+1

if ans%2==1:
    ans=ans//2 +1
else:
    ans=ans//2

print(ans)