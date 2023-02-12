import sys
input = sys.stdin.readline

nums = set()
for i in range(3, 1000, 2):
    tmp = 0
    for j in range(3, int(i**0.5) + 1):
        if i % j == 0:
            tmp = 1
            break
    if tmp == 0:
        nums.add(i)
print(nums)
while True:
    n = int(input())
    a, b = 0, 0
    if n == 0:
        break
    for i in range(3, 1000000, 2):
        if n // 2 + 1 < i:
            break
        if i in nums and n - i in nums:
                a = i
                b = n - i
                break
    if a == 0:
        print('Goldbach\'s conjecture is wrong.')
    else:
        print(f'{n} = {a} + {b}')