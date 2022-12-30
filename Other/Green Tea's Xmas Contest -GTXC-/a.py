N = int(input())
R = list(map(int, input().split()))
B = list(map(int, input().split()))
R.sort()
B.sort()
ans = 'Yes'
if R != B:
    ans = 'No'
print(ans)
