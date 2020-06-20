n=int(input())
buka=[]
salary=[0]*(n-1)
for _ in range(n-1):
    buka.append(int(input()))

def my_index_multi(l, x):
    return [i for i, _x in enumerate(l) if _x == x]

def kane(num):
    bukazu=my_index_multi(buka,num)

    if len(bukazu)!=0:
        for i in bukazu:
            kane(i+2)
        max_sa=max([ salary[j] for j in bukazu])
        min_sa=min([ salary[j] for j in bukazu])
        salary[num-2] = max_sa + min_sa + 1

    else:
        salary[num-2]=1

if n>=2:
    for i in range(2,n+1):
        if salary[i-2]!=0:
            continue
        else:
            kane(i)

t_buka=my_index_multi(buka,1)

ans=max([ salary[j] for j in t_buka]) +  min([ salary[j] for j in t_buka]) + 1

print(ans)