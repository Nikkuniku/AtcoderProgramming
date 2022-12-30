k=int(input())

if k<=9:
    print(k)
    exit(0)

ans=[1,2,3,4,5,6,7,8,9]

i=0
while len(ans)<k:
    v=str(ans[i])
    n=len(v)
    #最後の桁
    v_last=int(v[-1])

    if v_last==0:
        ans.append(int(v+'0'))
        ans.append(int(v+'1'))
    elif v_last==9:
        ans.append(int(v+'8'))
        ans.append(int(v+'9'))
    else:
        ans.append(int(v+str(v_last-1)))
        ans.append(int(v+str(v_last)))
        ans.append(int(v+str(v_last+1)))
    i+=1

print(ans[k-1])





