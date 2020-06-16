c=int(input())

box=[]
for _ in range(c):
    b=list(map(int,input().split()))
    b=sorted(b,reverse=True)

    box.append(b)

a=max([i[0] for i in box])
b=max([j[1] for j in box])
c=max([k[2] for k in box])

print(a*b*c)