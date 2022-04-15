from csv import list_dialects

a=list(map(int,input().split()))

ans=0
for i in range(3):
    ans=a[ans]
print(ans)