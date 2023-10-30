X,Y=map(int,input().split())
ans='No'
if X<Y:
    if Y-X<=2:
        ans='Yes'
else:
    if X-Y<=3:
        ans='Yes'
print(ans)
