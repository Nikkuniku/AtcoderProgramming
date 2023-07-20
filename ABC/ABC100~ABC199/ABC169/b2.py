N=int(input())
A=sorted(list(map(int,input().split())))
ans=1
C=pow(10,18)
for a in A:
    ans*=a
    if ans>C:
        ans=-1
        break
print(ans)
    