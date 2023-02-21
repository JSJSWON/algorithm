N = int(input())
print('long ' * (N // 4 if N % 4 == 0 else N // 4 + 1) + 'int')