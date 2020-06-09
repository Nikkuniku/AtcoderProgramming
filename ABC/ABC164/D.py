S=input()
N=len(S)
cnt=0

for i in range(N-3):
    for j in range(i+4,N+1):
        if int(S[i:j])%2019 ==0:
            cnt+=1
            continue


print(cnt)
