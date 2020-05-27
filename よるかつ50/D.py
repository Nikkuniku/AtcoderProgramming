n=int(input())
a= list(map(int,input().split()))

rain = sum(a)/2

dam=[0]*n

for i in range(n):
    if i!=n-1:
        dam[i] = int((rain - a[i+1])*2)
    else:
        dam[i] = int((rain - a[0])*2)

print(*dam)
