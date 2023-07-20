n= int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

candy=[a,b]
n_i=0
n_j=0

score=0
for i in range(n):
    tmp_a = a[:i+1]
    tmp_b = b[i:]
    tmp_score = sum(tmp_a) + sum(tmp_b)

    score = max(score,tmp_score)


print(score)
