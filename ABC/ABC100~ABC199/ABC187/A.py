a,b=input().split()

ans1=0
ans2=0
for i in list(a):
    ans1+=int(i)

for j in list(b):
    ans2+=int(j)

if ans1>=ans2:
    print(ans1)
else:
    print(ans2)