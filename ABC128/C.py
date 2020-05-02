N,M = map(int,input().split())

SwitchCond=[]
for i in range(M):
    k_i = list(map(int,input().split()))
    k_i = k_i[1:]
    SwitchCond.append(k_i)

Lights = list(map(int,input().split()))


cnt=0

for i in range(2**N):
    Ans=[0]*M
    i = format(i,'0{}b'.format(N))

    for k in range(M):
        light_num=0
        for n in SwitchCond[k]:
            if i[n-1]=='1':
                light_num+=1
        
        if light_num%2==Lights[k]:
            Ans[k]=1
    
    if sum(Ans)==M:
        cnt+=1

print(cnt)
