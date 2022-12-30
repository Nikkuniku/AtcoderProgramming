N,K=map(int,input().split())

from collections import Counter

snuke_s = set([i for i in range(1,N+1)])

s=set()

for i in range(K):
    d_i = int(input())
    snuke = set(list(map(int,input().split())))

    s=s|snuke

s_diff = snuke_s - s

print(len(s_diff))