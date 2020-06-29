n=int(input())
s=input()

s=list(map(int,list(s)))

password=[str(i).zfill(3) for i in range(1000)]

cnt=0
can=[]
for word in password:
    w1=int(word[0])
    w2=int(word[1])
    w3=int(word[2])

    i=0
    while i<n-2:
        if s[i]==w1:
            i_1=i
            break
        else:
            i+=1

        if i==n-3 and s[i]!=w1:
            i_1=-1
            break
    
    if i_1==-1:
        continue

    j=i+1
    while j<n-1:
        if s[j]==w2:
            i_2=j
            break
        else:
            j+=1

        if j==n-2 and s[j]!=w2:
            i_2=-1
            break
    
    if i_2==-1:
        continue

    k=j+1
    while k<n:
        if s[k]==w3:
            i_3=k
            break
        else:
            k+=1
        
        if k>=n-1 and s[n-1]!=w3:
            i_3=-1
            break

    if i_3==-1:
        continue
    elif i_1<i_2 and i_2<i_3:
        cnt+=1
        can.append(word)


print(cnt)
