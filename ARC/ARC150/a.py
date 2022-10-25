def judge(s, K):
    init_1 = s.count('1')
    from collections import deque, defaultdict
    q = deque()
    d = defaultdict(int)
    cnt = 0
    for i in range(len(s)):
        q.append(s[i])
        d[s[i]] += 1
        if len(q) == K:
            if d['0'] > 0:
                pass
            else:
                if d['1']+d['?'] == K and d['?'] <= K-init_1:
                    cnt += 1
            d[q.popleft()] -= 1
    if cnt == 0 or cnt > 1:
        return False
    else:
        return True


T = int(input())
ans = []
for _ in range(T):
    n, k = map(int, input().split())
    s = input()
    if judge(s, k):
        ans.append('Yes')
    else:
        ans.append('No')
print(*ans, sep="\n")
