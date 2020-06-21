n=int(input())

d={}

for _ in range(n):
    s=input()

    if s in d:
        d[s]+=1
    else:
        d[s]=1

max_k = max(d,key=d.get)

print(max_k)