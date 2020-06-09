r,g,b,n = map(int,input().split())


cnt=0
for i in range(n+1):
    for j in range(n+1):

        hB = n - (r*i) - (j*g)

        if hB >= 0 and hB%b==0:
            cnt+=1

print(cnt)
