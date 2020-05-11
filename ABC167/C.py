n,m,x = map(int,input().split())

books=[]

for _ in range(n):
    books.append(list(map(int,input().split())))

cost = 10**18
for i in range(2**n):

    i = format(i,'0{}b'.format(n))

    flg =0
    total =0
    skill=[0]*m
    for j in range(n):
        if i[j]=='1':
            book_j = books[j]
            
            total += book_j[0]

            for l in range(len(book_j)):
                if l==0:
                    continue
                else:
                    skill[l-1]+=book_j[l]

    for k in range(m):
        if skill[k]<x:
            flg+=1
    
    if flg==0:
        cost = min(cost,total)

if cost==10**18:
    print(-1)
else:
    print(cost)