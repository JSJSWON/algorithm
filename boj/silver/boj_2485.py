import sys
input = sys.stdin.readline

n = int(input())
trees = []
for _ in range(n):
    trees.append(int(input()))

trees.sort()

gap = []

for i in range(len(trees)-1):
    gap.append(trees[i+1] - trees[i])


def gcd_(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def gcd_n(arr):
    gcd = arr[0]
    for x in arr:
        gcd = gcd_(gcd, x)
    return gcd


print((trees[-1] - trees[0]) // gcd_n(gap) - len(gap))
