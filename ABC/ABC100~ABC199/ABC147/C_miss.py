N=int(input())

Honests =['']*N

for i in range(N):
    
    A_i = int(input())
    
    for j  in range(A_i):

        x_ij,y_ij = map(int,input().split())
        x_ij=x_ij-1

        if y_ij==0:
            Honests[x_ij] += '0'
        else:
            Honests[x_ij] += '1'

print(Honests) 

cnt=0
cnt_0=0
cnt_un=0

for i in Honests:
    cnt += i.count('1')
    cnt_0 += i.count('0')
    if '' == i:
        cnt_un+=1

if cnt==0 and cnt_0>0:
    print(0)
    exit(0)

print(cnt-(cnt_0-cnt_un))

