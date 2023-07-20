S, T, X = map(int, input().split())
time = [0]*48
if S < T:
    for t in range(2*S, 2*T):
        time[t] = 1
else:
    for t in range(2*S, 48):
        time[t] = 1
    for t in range(2*T):
        time[t] = 1
ans = 'No'
if time[2*X+1]:
    ans = 'Yes'
print(ans)
