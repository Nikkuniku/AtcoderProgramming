q,h,s,d = map(int,input().split())
n=int(input())

ans=0
if n==1:
    ans = min((s,2*h,4*q))
else:
    arr=[d/2,4*q,2*h,s]
    i = arr.index(min(arr))

    if n%2==0:
        ans += arr[i]*n
    else:
        if i==0:
            ans += (n//2)*d
            arr.pop(i)

            i = arr.index(min(arr))
            ans+=arr[i]
        else:
            ans+=arr[i]*n

print(int(ans))