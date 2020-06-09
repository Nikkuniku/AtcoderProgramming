n=int(input())

a=[]
b=[]

for _ in range(n):
    a_i ,b_i = map(int,input().split())

    a.append(a_i)
    b.append(b_i)

cnt=0

a=list(reversed(a))
b=list(reversed(b))


for i in range(n):
    fr = a[i]+cnt
    target =b[i]

    if fr ==0 or target==1 or fr%target ==0:
        continue

    num = abs(target -fr) // target

    if fr>target:
        target += target*(num+1)
    
    cnt += (target-fr)

print(int(cnt))
        

