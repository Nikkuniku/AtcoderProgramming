n,p=map(int,input().split())

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

arr=factorization(p)

ans=1
for i in range(len(arr)):
    if arr[i][1]//n!=0:
        ans*=arr[i][0]**(arr[i][1]//n)

if p==1:
    ans=1
elif n==1:
    ans=p


print(ans)