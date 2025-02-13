N = int(input())
Segment = [list(map(int, input().split())) for _ in range(N)]
Segment.sort(key=lambda x: x[1])
Segment.sort(key=lambda x: x[0])
