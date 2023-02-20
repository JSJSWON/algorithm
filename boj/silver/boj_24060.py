n, k = map(int, input().split())

a = list(map(int, input().split()))

save = []


def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


def merge(A, p, q, r):
    global save

    i, j = p, q + 1
    tmp = []

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    while i <= q:
        tmp.append(A[i])
        i += 1

    while j <= r:
        tmp.append(A[j])
        j += 1

    i, t = p, 0
    while i <= r:
        A[i] = tmp[t]
        i += 1
        t += 1
    save += tmp


merge_sort(a, 0, len(a)-1)

try:
    print(save[k-1])
except IndexError:
    print(-1)
