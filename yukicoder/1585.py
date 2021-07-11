n=int(input())

ans='No'
for i in range(1,10**6 + 1):
    if pow(i,3)==n:
        ans='Yes'
        break

print(ans)