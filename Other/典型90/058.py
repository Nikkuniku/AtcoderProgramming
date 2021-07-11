n,k=map(int,input().split())
mod=10**5
s=set()

arr=[n]
while True:
    x = arr[-1]
    y = sum(map(int,list(str(x))))
    z = (x+y)%mod

    if z in s:
        break
    else:
        arr.append(z)
        s.add(z)

i=0
while True:
    if arr[i]==z:
        break
    i+=1

roopLen = len(arr)-i

if k<len(arr):
    print(arr[k])
else:
    p = (k-i)%roopLen
    ans = i+p
    print(arr[ans])