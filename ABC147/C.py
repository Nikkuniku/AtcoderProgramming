N=int(input())

A=[]
test = []
for i in range(N):
    A_i= int(input())
    A.append(A_i)
    for j in range(A_i):
        x,y= map(int,input().split())

        test.append([x-1,y])

print(A)
print(test)

total = 0
for i in range(2**N):
    
    Honests=[0]*N
    
    for j in range(N):

        if (i>>j) &1:

            A_j = A[j]
            
            for k in range(A_j):
                x,y =test[j][0],test[j][1]

                x-=1
                if y ==1:
                    Honests[x]=1
                else:
                    Honests[x]=0
        else:
            A_j=A[j]

            for k in range(A_j):
                x,y =test[j][0],test[j][1]

                x-=1
                if y ==1:
                    Honests[x]=0
                else:
                    Honests[x]=1
            
    total = max(total,max(Honests))

print(total)


