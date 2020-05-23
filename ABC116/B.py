s=int(input())

def collatz(n):
    if n%2==0:
        return int(n/2)
    else:
        return 3*n + 1

d={}
for i in range(10000001):
    d[i]=0

now =s
d[now]=1
num =1
while True:

    now = collatz(now)
    num +=1

    if d[now]!=0:
        print(num)
        exit(0)
    else:
        d[now]+=1
