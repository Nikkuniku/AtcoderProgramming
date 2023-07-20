S = input()
ans = 'Yes'
if not (('N' in S and 'S' in S) or ('N' not in S and 'S' not in S)):
    ans = 'No'
if not (('W' in S and 'E' in S) or ('W' not in S and 'E' not in S)):
    ans = 'No'
print(ans)
