n,a,b,c,d = map(int,input().split())
s = input()

from itertools import groupby 

gr = groupby(s)

#AからCへいけるかどうか
for i in range(a-1,c-1):
    if s[i]=='#' and s[i+1]=='#':
        print('No')
        exit(0)
#BからDへいけるかどうか
for i in range(b-1,d-1):
    if s[i]=='#' and s[i+1]=='#':
        print('No')
        exit(0)


if c<b:
    print('Yes')
else:
    if c<d:
        print('Yes')
    else:
        for i in range(b-2,d-1):
            if s[i]=='.' and s[i+1]=='.' and s[i+2]=='.':
                print('Yes')
                exit(0)        
        print('No')
