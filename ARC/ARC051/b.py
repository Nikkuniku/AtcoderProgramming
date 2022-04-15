k=int(input())

r=0
b=1
a=2
for i in range(k):
    if i==0:
        continue
    else:
        r,b=b,a
        a=r+b
print(a,b)


cnt=0
def gcd(a,b):
    global cnt
    if b==0:
        return a
    cnt+=1
    if b>a:
        a,b=b,a
    return gcd(a,a%b)
gcd(a,b)
print(cnt)