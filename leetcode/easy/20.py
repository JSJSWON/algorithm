# 나의 풀이
class Solution:
    def isValid(self, s: str) -> bool:
        b = {'(': ')', '{': '}', '[': ']'}
        stack = []
        s = list(s)

        while s:
            tmp = s.pop()
            if stack:
                if tmp in b:
                    if stack[-1] == b[tmp]:
                        stack.pop()
                        continue
            stack.append(tmp)
        return not stack


# 책의 풀이
# class Solution:
#     def isValid(self, s: str) -> bool:
#         b = {')': '(', '}': '{', ']': '['}
#         stack = []
#
#         for char in s:
#             if char not in b:
#                 stack.append(char)
#             elif not stack or b[char] != stack.pop():
#                 return False
#         return not stack


sol = Solution()
s = "()"
print(sol.isValid(s))
