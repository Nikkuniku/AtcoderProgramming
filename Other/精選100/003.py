s=input()
from collections import deque
q=deque()

ans=0
for i in range(len(s)):
    tmp=0
    for j in range(i,len(s)):
        if s[j] in ['A','C','G','T']:
            tmp+=1
        else:
            break
    ans=max(tmp,ans)
print(ans)