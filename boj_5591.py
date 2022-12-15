nums = []
for _ in range(28):
    num = int(input())
    nums.append(num)
for x in [i for i in range(1, 31) if i not in nums]:
    print(x)