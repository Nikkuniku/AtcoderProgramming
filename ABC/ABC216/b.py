n=int(input())
name=[]
for _ in range(n):
    s=input()
    name.append(s)

ans='No'
for i in range(n):
    for j in range(i+1,n):
        if name[i]==name[j]:
            ans='Yes'
            break

print(ans)
