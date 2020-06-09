N=int(input())

A=[]
test = []
for i in range(N):
    A_i= int(input())
    A.append(A_i)
    testimony_i=[]
    for j in range(A_i):
        x,y= map(int,input().split())

        testimony_i.append([x,y])
    
    test.append(testimony_i)

total=0
for i in range(2**N):

    member = format(i,'0{}b'.format(N))

    flg = 0

    for j in range(N):
        if member[j]== '1':

            syogen = test[j]

            for s in syogen:
                if member[s[0]-1]==str(s[1]):
                    continue
                else:
                    flg+=1

    if flg ==0:
        total = max(total , member.count('1')) 

print(total)


