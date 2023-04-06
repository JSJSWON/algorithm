# 재귀 풀이
# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
#         for char in sorted(set(s)):
#             suffix = s[s.index(char):]
#             print(char, suffix, s)
#             if set(s) == set(suffix):
#                 return char + self.removeDuplicateLetters(suffix.replace(char, ''))
#         return ''  # 마지막 글자


import collections


# 스택 풀이
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            # stack[-1] got popped because char < stack[-1] and stack[-1] is gonna repeat in future
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)


sol = Solution()
s = "cbacdcbc"
print(sol.removeDuplicateLetters(s))
