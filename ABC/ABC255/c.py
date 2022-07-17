x, a, d, n = map(int, input().split())
y = x-a
if d == 0:
    ans = abs(x-a)
else:
    if d > 0:
        if y <= 0:
            ans = abs(y)
        elif y >= (n-1)*d:
            ans = abs(y-((n-1)*d))
        else:
            p = y//d
            ans = min(abs(y - (p*d)), abs(y-((p+1)*d)),
                      abs(y-((p-1)*d)))
    else:
        if y >= 0:
            ans = abs(y)
        elif y <= (n-1)*d:
            ans = abs((n-1)*d-y)
        else:
            p = -y//abs(d)
            ans = min(abs(y-(p*d)), abs(y-((p+1)*d)),
                      abs(y-((p-1)*d)))
print(ans)
