n=int(input())
x=list(map(int,input().split()))

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

# 全ての約数を求める
divisors=set()

for i in range(n):
    tmp=factorization(x[i])
    for j in range(len(tmp)):
        divisors.add(tmp[j][0])
divisors.discard(1)
divisors=sorted(list(divisors))
cnt=0
d={}
p=0
for i in range(n):
    if x[i] not in d:
        d[x[i]]=False
        p+=1
ans=1
j=0
while cnt<p:
    tmp=0   
    for k in range(n):
        if d[x[k]]==True:
            continue
        else:
            if x[k]%divisors[j]==0:
                cnt+=1
                tmp+=1
                d[x[k]]=True

    if tmp>0:
        ans*=divisors[j]
    j+=1

print(ans)