word=['q','w','y','p','d','f','j','l','z','x','v']

for i in range(len(word)):
    for j in range(i+1,len(word)):
        ans='a'+word[i]+'o'+word[j]+'t'
        print(ans)