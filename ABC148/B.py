N=int(input())
S,T=input().split()

strings =''

for i in range(N):
    strings+=S[i]
    strings+=T[i]

print(strings)