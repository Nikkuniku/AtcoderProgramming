N, T, A = map(int, input().split())
diff = N - (T + A)
ans = "Yes"
if T + diff > A and A + diff > T:
    ans = "No"
print(ans)
