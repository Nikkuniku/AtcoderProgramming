N,M=map(int,input().split())

d={}

condi = []

string = ['0']*N

flg=0
for _ in range(M):
    s,c = map(int,input().split())

    condi.append([s,c])

    if s not in d:
        d[s]=c
    elif s in d :
        if d[s]!=c:
            flg+=1

if flg!=0:
    print(-1)
    exit(0)

if 1 in d:
    if d[1]==0 and N!=1:
        print(-1)
        exit(0)

if N==1 and M==0:
    print(0)
    exit(0)

for i in range(N):
    if i==0 and 1 not in d :
        string[0] = '1'
    else:
        if i+1 in d:
            string[i] = str(d[i+1])

str_num = ''.join(string)
print(str_num)