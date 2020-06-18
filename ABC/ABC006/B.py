n=int(input())

a=[0,0,1]
mod=10007
if n>=4:
    for i in range(n-3):
        a.append(a[i]%mod+a[i+1]%mod+a[i+2]%mod)


print(a[n-1]%mod)
