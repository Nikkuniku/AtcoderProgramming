n=int(input())
a= list(map(int,input().split()))

s = sum(a)

ans= 10**18

subtotal = 0
for i in range(n-1):
    subtotal+=a[i]

    ans = min(ans,abs(subtotal - (s - subtotal)))


print(ans)
