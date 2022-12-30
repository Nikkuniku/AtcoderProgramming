d={"H":0 , "2B":0 , "3B":0 , "HR":0}

ans='Yes'
for _ in range(4):
    s=input()
    d[s]+=1


for k,v in d.items():
    if v==1:
        continue
    else:
        ans='No'
        break
print(ans)
