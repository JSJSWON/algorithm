n = int(input())
cnt = [0, 0]
for i in range(2, 10**6 + 1):
    tmp = []
    if i % 3 == 0:
        tmp.append(cnt[i//3])
    if i % 2 == 0:
        tmp.append(cnt[i//2])
    tmp.append(cnt[i-1])

    cnt.append(min(tmp)+1)
print(cnt[n])

ans = ''
index = n
while index != 1:
    ans += f'{index} '
    tmp = []
    if index % 3 == 0:
        tmp.append(cnt[index//3])
    else:
        tmp.append(10**7)
    if index % 2 == 0:
        tmp.append(cnt[index//2])
    else:
        tmp.append(10**7)
    tmp.append(cnt[index-1])
    if tmp.index(min(tmp)) == 0:
        index //= 3
    elif tmp.index(min(tmp)) == 1:
        index //= 2
    else:
        index -= 1
ans += '1'
print(ans)