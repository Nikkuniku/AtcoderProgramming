n,k=map(int,input().split())
a=list(map(lambda x: abs(int(x)),input().split()))
mod = 10**9 + 7
positive=list()
negative=list()


for i in range(n):
    if a[i]>=0:
        positive.append(a[i])
    else:
        negative.append(a[i])


if len(positive)==0:
    negative=sorted(negative,reverse=True)
    cnt=0
    ans=1
    for i in negative:
        if cnt<k:
            ans*=i
            cnt+=1    

    if cnt<k:
        ans=0
    print(ans%mod)
    exit(0)

positive=sorted(positive,reverse=True)
negative=sorted(negative)


from collections import deque

ans=deque([])
positive=deque(positive)
negative=deque(negative)



while len(ans)<k:
    if len(positive)!=0:
        posi=positive.popleft()
    else:
        posi=0
    
    if len(negative)!=0:
        nega=negative.popleft()
    else:
        nega=0

    if posi>=abs(nega):
        ans.append(posi)
        
        negative.appendleft(nega)

    elif posi<abs(nega):
        ans.append(nega)
        ans.append(negative.popleft())

        positive.appendleft(posi)

    
    if len(ans)>k:
        ans.pop()
        ans.pop()
        ans.append(posi)

answer=1

for j in ans:
    answer*=j

print(answer%mod)


