N, A, B = map(int, input().split())
D = list(map(int, input().split()))
if N == 1:
    exit(print("Yes"))
C = [d % (A + B) for d in D]
C.sort()
diff = []
for i in range(N - 1):
    diff.append(C[i + 1] - C[i])
diff.append((C[0] - C[N - 1]) % (A + B))
ans = "Yes" if max(diff) > B or max(diff) == 0 else "No"
print(ans)
