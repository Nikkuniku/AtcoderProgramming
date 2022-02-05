n,q=map(int,input().split())
a=list(map(int,input().split()))
a=sorted(a)
answers=[]
import bisect
for _ in range(q):
    x=int(input())

    index = bisect.bisect_left(a,x)

    ans = n-index
    answers.append(ans)

print(*answers,sep="\n")
