R, C, rs, cs, rt, ct = map(int, input().split())
ans = 0
for r in range(1, R+1):
    if r == rs:
        continue
    elif r == rt:
        continue
    else:
        if 1 <= abs(r-rs) <= abs(ct-cs):
            ans += 2
        else:
            if cs < ct and ct-abs(r-rs) >= 1:
                ans += 1
            elif ct < cs and ct+abs(r-rs) <= C:
                ans += 1
for c in range(1, C+1):
    if c == cs or c == ct:
        continue
    else:
        if 1 <= abs(c-cs) <= abs(rt-rs):
            ans += 2
        else:
            if rs < rt and rt-abs(c-cs) >= 1:
                ans += 1
            elif rt < rs and rt+abs(c-cs) <= R:
                ans += 1
naname = 0
naname += min(rt-1, ct-1)
naname += min(R-rt, ct-1)
naname += min(R-rt, C-ct)
naname += min(rt-1, C-ct)
ans += naname*2
print(ans)
print(naname)
