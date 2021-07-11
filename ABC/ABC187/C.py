n=int(input())
s=[]
for _ in range(n):
    s.append(input())

s=sorted(s,reverse=True)

d={}
ans='satisfiable'
for i in range(n):
    T=s[i]

    if T[0]!='!':
        d[T]=1
    elif T[0]=='!':
        if T[1:] in d:
            ans=T[1:]
            break


print(ans)