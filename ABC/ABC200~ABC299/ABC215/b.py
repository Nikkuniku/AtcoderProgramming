n=int(input())

ans=0
for i in range(100):
    ans=i
    if pow(2,ans)>n:
        break

print(ans-1)