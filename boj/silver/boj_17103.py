def prime_list(n):
    prime = [1 for _ in range(n + 1)]
    prime[0], prime[1] = 0, 0
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            j = 2
            while True:
                tmp = i * j
                if tmp > n:
                    break
                prime[tmp] = 0
                j += 1
    return prime


primes = prime_list(1000000)
t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    for i in range(n // 2 + 1):
        if primes[i] and primes[n - i]:
            cnt += 1
    print(cnt)
