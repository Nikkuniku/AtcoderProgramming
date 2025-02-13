N = int(input())
P = [str(i + 1).zfill(3) for i in range(60)]
P.remove("042")
ans = "AGC" + P[N - 1]
print(ans)
