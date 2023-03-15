x, y = map(int, input().split())

# z = int((y / x) * 100) 틀림
'''
실수 오차라는 건 어떻게 일어날지 알아내기가 굉장히 어렵습니다.
아주 대충만 말씀드리자면, 틀린 코드는 실수 연산을 두 번 하게 되고, 맞은 코드는 한 번만 하기 때문에 틀린 코드가 
조금 더 부정확해질 가능성이 높습니다.
https://www.acmicpc.net/board/view/53623
'''
z = int(y * 100 / x)

left, right = 1, 1000000000

while left <= right:
    mid = (left + right) // 2
    ratio = int((y + mid) * 100 / (x + mid))
    if z != ratio:
        right = mid - 1
    else:
        left = mid + 1

if left == 1000000001:
    print(-1)
else:
    print(left)
