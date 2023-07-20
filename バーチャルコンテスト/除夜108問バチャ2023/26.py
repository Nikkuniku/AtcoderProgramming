N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 'No'
for i, v in enumerate(A):
    if v == max(A):
        if i+1 in B:
            ans = 'Yes'
            break
print(ans)
