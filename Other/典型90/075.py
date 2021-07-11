n=int(input())
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

arr=factorization(n)

from math import ceil,log2

ans=0

c=0
for i in range(len(arr)):
    c+=arr[i][1]

if c==1:
    pass
else:
    ans=ceil(log2(c))


print(ans)