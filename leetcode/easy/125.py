class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for letter in s:
            if letter.isalnum():
                new_s += letter.lower()
        return new_s == new_s[::-1]


sol = Solution()
example = "0P"
print(sol.isPalindrome(example))
