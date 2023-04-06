from typing import List


# 나의 풀이
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = []
        temperatures = temperatures[::-1]
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append(i)
                answer.append(0)
            else:
                if temp >= temperatures[stack[-1]]:
                    while stack:
                        if temp < temperatures[stack[-1]]:
                            break
                        if stack:
                            stack.pop()
                    if not stack:
                        answer.append(0)
                    else:
                        answer.append(i - stack[-1])
                else:
                    answer.append(1)
                stack.append(i)
        return answer[::-1]


# 책의 풀이
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         answer = [0] * len(temperatures)
#         stack = []
#         for i, cur in enumerate(temperatures):
#             while stack and cur > temperatures[stack[-1]]:
#                 last = stack.pop()
#                 answer[last] = i - last
#             stack.append(i)
#         return answer


sol = Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(sol.dailyTemperatures(temperatures))
