n=int(input())
d={}

for i in range(n):
    s=input()

    if s in d:
        continue
    else:
        print(i+1)
        d[s]=1
