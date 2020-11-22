a,b,c =map(int,input().split())

s=a+b+c

p=(100-a)*a/s
q=(100-b)*b/s
r=(100-c)*c/s

ans=p+q+r

print(ans)