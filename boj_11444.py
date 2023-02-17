n = int(input())

def devide(n):
    steps = []
    while n != 1:
        if n % 2 == 1:
            steps.append(1)
        else:
            steps.append(0)
        n //= 2
    return steps

def conquer(steps):
    p = 1000000007
    m = [[1, 1], 
         [1, 0]]
    answer = [[1, 1],
              [1, 0]]
    for step in steps[::-1]:
        x1 = answer[0][0] * answer[0][0] + answer[0][1] * answer[1][0]
        x2 = answer[0][0] * answer[0][1] + answer[0][1] * answer[1][1]
        x3 = answer[1][0] * answer[0][0] + answer[1][1] * answer[1][0]
        x4 = answer[1][0] * answer[0][1] + answer[1][1] * answer[1][1]
        answer = [[x1 % p, x2 % p],
                  [x3 % p, x4 % p]]
        if step == 1:
            x1 = answer[0][0] * m[0][0] + answer[0][1] * m[1][0]
            x2 = answer[0][0] * m[0][1] + answer[0][1] * m[1][1]
            x3 = answer[1][0] * m[0][0] + answer[1][1] * m[1][0]
            x4 = answer[1][0] * m[0][1] + answer[1][1] * m[1][1]
            answer = [[x1 % p, x2 % p],
                      [x3 % p, x4 % p]]
    return answer

print(conquer(devide(n))[0][1])