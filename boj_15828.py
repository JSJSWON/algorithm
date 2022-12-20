from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()

while True:
    p = int(input())
    if p == -1:
        if len(queue) == 0:
            print('empty')
        else:
            ans = ''
            for x in queue:
                ans += f'{x} '
            ans.rstrip()
            print(ans)
        break
    elif p == 0:
        queue.popleft()
    else:
        if len(queue) == N:
            continue
        queue.append(p)