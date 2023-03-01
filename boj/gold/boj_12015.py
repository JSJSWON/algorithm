N = int(input())
A = map(int, input().split())
LIS = [0]

'''
만약 LIS = [0, 10, 30]인데
x = 10이면 LIS 안에서 이분탐색을 통해 right = 1, LIS[right] = 10이라는 결과가 나옴
x = 15이면 LIS 안에서 이분탐색을 통해 right = 2, LIS[right] = 15라는 결과가 나옴 -> LIS[2]가 30에서 15로 대체됨
x = 40이면 이분탐색을 하지 않고 바로 LIS로 append됨

만약 A = [0, 10, 30, 15]라면
LIS는 [0, 10, 30]과 [0, 10, 15]가 가능하다.
하지만 아래의 방법을 이용하면 [0, 10, 15]만 나오게 된다.
'''

for x in A:
    if x > LIS[-1]:
        LIS.append(x)
    else:
        left, right = 0, len(LIS)
        while True:
            if left >= right:
                break
            mid = (left + right) // 2
            if x > LIS[mid]:
                left = mid + 1
            else:
                right = mid
        LIS[right] = x

print(len(LIS)-1)
