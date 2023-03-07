from itertools import combinations

n, c = map(int, input().split())

w = list(map(int, input().split()))
mid = n // 2 + 1 if n % 2 == 1 else n // 2
front, back = w[:mid], w[mid:]


def weights(w):
    length = len(w)
    if length == 0:
        return []
    ws = []
    for i in range(1, length + 1):
        ws += [sum(x) for x in combinations(w, i) if sum(x) <= c]
    return ws


# num보다 큰 애 중 제일 작은 애를 찾아야 함
def binary_search(w, num):
    if len(w) == 0 or w[0] > num:
        return 0
    if w[-1] <= num:
        return len(w)

    left, right = 0, len(w)
    while True:
        if w[left] > num:
            return left
        mid = (left + right) // 2
        if w[mid] <= num:
            left = mid + 1
        else:
            right = mid - 1


ws_front = sorted(weights(front))
ws_back = weights(back)
ans = len(ws_front) + len(ws_back)

for x in ws_back:
    ans += binary_search(ws_front, c-x)

print(ans + 1) # 아무것도 넣지 않은 경우 추가
