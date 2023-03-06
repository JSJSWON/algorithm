a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

a2 = c - a1

if a2 < 0:
    print(0)
elif a2 == 0:
    if a0 <= 0:
        print(1)
    else:
        print(0)
else:
    a3 = a0 / a2
    if a3 <= n0:
        print(1)
    else:
        print(0)
