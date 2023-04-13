from typing import List


# 반복문 풀이(나의 풀이)
class Solution:
    def twoletters(self, a, b, digit):
        ans = []
        for aa in a:
            for bb in b:
                ans.append(aa + bb)
        return ans

    def letterCombinations(self, digits: str) -> List[str]:
        digit = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return digit[digits]
        ans = digit[digits[0]]
        for i in range(1, len(digits)):
            ans = self.twoletters(ans, digit[digits[i]], digit)
        return ans


# 재귀 풀이(책의 풀이)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return

            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)

        if not digits:
            return []

        dic = {'2': 'abc',
               '3': 'def',
               '4': 'ghi',
               '5': 'jkl',
               '6': 'mno',
               '7': 'pqrs',
               '8': 'tuv',
               '9': 'wxyz',
               }
        result = []
        dfs(0, '')

        return result


sol = Solution()
digits = '23'
print(sol.letterCombinations(digits))
