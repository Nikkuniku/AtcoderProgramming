b=list(input().split())
n=int(input())

d={}
for i in range(10):
    d[b[i]]=str(i)

ans=[]
for _ in range(n):
    num=input()

    tmp=''
    for s in num:
        tmp+=d[s]

    ans.append([int(num),int(tmp)])   

ans=sorted(ans,key=lambda x: x[1])

for i in range(n):
    print(ans[i][0])