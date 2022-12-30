N, L = map(int, input().split())
A = list(map(int, input().split()))
ans = 'Yes'
for i in range(N):
    if A[i] == 1:
        if L >= 2:
            L -= 2
        else:
            L -= 1
    else:
        if L >= 3:
            L -= 3
        elif L >= 2:
            L -= 2
        else:
            ans = 'No'
            break
print(ans)
