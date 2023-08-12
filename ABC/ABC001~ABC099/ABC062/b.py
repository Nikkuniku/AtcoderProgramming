H,W=map(int,input().split())
ans=[['#']*(W+2)]
for _ in range(H):
    ans.append(['#']+input().split()+['#'])
ans.append(['#']*(W+2))
for c in ans:
    print(''.join(c))
    