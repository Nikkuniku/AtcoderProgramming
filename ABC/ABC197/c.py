import sys
n=int(input())
a=list(map(int,sys.stdin.readline().split()))
if n<2:
    ans=a[0]
else:
    ans = 1<<31
    for i in range(1,2**(n-1)):
        XOR=0
        OR=a[n-1]
        for j in range(n-1):
            if ((i>>j)&1):
                XOR^=OR
                OR=a[n-1-j-1]
            else:
                OR|=a[n-1-j-1]
        XOR^=OR
        ans= min(XOR,ans)
        
print(ans)