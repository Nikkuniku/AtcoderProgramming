n=int(input())

d={}

for _ in range(n):
    s=input()

    d[s[::-1]]=s
d =sorted(d.items(),key=lambda x: x[0])

for i in range(n):
    print(d[i][1])