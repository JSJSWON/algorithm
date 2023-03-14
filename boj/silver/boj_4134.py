import sys
input = sys.stdin.readline


def prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    tmp = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            tmp += 1
            break
    if tmp == 0:
        return True
    return False


n = int(input())

for _ in range(n):
    num = int(input())
    while True:
        if prime(num):
            print(num)
            break
        else:
            num += 1
