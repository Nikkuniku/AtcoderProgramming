N,M = map(int,input().split())

d_1=[0]*N
d_2=[0]*N

for i in range(M):
    p_i,S_i = input().split()
    p_i =int(p_i)-1
    if S_i=='WA' and d_2[p_i]==0:
        d_1[p_i]+=1
    elif S_i=='AC' and d_2[p_i]==0:
        d_2[p_i]=1

penalty=0
for j in range(N):
    if d_2[j]==1:
        penalty+=d_1[j]

print(sum(d_2),penalty)

