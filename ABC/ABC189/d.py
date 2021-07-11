from os import truncate


n=int(input())
operation=[]
for _ in range(n):
    operation.append(input())
operation=list(reversed(operation))
operation.append('r')
answer=0
def rec(o,k,m):
    global answer
    ans=0
    if o=='r':
        answer+=1
    
    if o=='OR' and k==True:
        rec(operation[m+1],True,m+1)
        rec(operation[m+1],False,m+1)
    elif o=='OR' and k ==False:
        rec(operation[m+1],False,m+1)
        rec(operation[m+1],True,m+1)
    elif o=='AND' and k==True:
        rec(operation[m+1],True,m+1)
    elif o=='AND' and k==False:
        rec(operation[m+1],False,m+1)
        rec(operation[m+1],True,m+1)

    return ans

print(operation)
print(rec(operation[0],True,0))
print(answer)