k=int(input())

if k<=9:
    print(k)
    exit(0)

ans=[1,2,3,4,5,6,7,8,9]

i=0
while len(ans)<k:
    v=ans[i]

    mod=v%10

    if mod==0:
        ans.append(10*v+mod)
        ans.append(10*v+mod+1)
    elif mod==9:
        ans.append(10*v+mod-1)
        ans.append(10*v+mod)
    else:
        ans.append(10*v+mod-1)
        ans.append(10*v+mod)
        ans.append(10*v+mod+1)

    i+=1

print(ans[k-1])

        

