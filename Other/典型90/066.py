n=int(input())
ran=[]
for _ in range(n):
    ran.append(list(map(int,input().split())))

ans=[]
for i in range(n-1):
    l_i =ran[i][0]
    r_i =ran[i][1]
    for j in range(i+1,n):
        cnt=0
        p=0
        l_j=ran[j][0]
        r_j=ran[j][1]
        for k in range(l_i,r_i+1):
            for m in range(l_j,r_j+1):
                p+=1
                if k>m:
                    cnt+=1
        
        ans.append(cnt/p)
print(sum(ans))