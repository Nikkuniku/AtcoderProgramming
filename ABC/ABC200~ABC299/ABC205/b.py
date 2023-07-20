N = int(input())
A = list(map(int, input().split()))
A.sort()
B = [i+1 for i in range(N)]
ans = 'No'
if A == B:
    ans = 'Yes'
print(ans)
