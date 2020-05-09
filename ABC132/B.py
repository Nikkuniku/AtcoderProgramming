n=int(input())

p = list(map(int,input().split()))

cnt = 0
for i in range(n-2):
    seq = p[i:i+3]
    
    a = seq[1]

    if sorted(seq)[1] == a:
        cnt+=1

print(cnt)
    
