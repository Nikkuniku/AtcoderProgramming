a=int(input())

f=[0,1,2]
i=3
fib=f[i-2]+f[-1]

ans=2
while fib<a:
    if fib%2==0:
        ans+=fib
    
    f.append(fib)
    i+=1
    fib=f[i-2]+f[-1]


print(f)
print(ans)