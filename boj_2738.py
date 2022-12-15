n, m = map(int, input().split())
A = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    A.append(tmp)
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        A[i][j] += tmp[j]
for i in range(n):
    ans = ''
    for j in range(m):
        ans += str(A[i][j]) + ' '
    print(ans.rstrip())