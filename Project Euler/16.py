n=int(input())

ans=pow(2,n)

ans=list(str(ans))

p=0
for i in range(len(ans)):
    p+=int(ans[i])

print(p)