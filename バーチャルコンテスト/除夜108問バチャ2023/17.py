N = int(input())
H = list(map(int, input().split()))
ans = H.index(max(H))+1
print(ans)
