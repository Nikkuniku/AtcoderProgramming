words = 'and,not,that,the,you'.split(',')
N = int(input())
W = input().split()
ans = 'No'
for w in W:
    if w in words:
        ans = 'Yes'
print(ans)
