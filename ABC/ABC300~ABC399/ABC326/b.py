N=int(input())
for i in range(N,1000):
    s=str(i)
    hyaku=int(s[0])
    ju=int(s[1])
    ichi=int(s[2])
    if hyaku*ju==ichi:
        break
print(i)