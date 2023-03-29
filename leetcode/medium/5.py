class Solution:
    def expand(s: str, left: int, right: int) -> str:
        ans = ''
        while right <= len(s):
            if s[left:right] == s[left:right][::-1]:
                ans = s[left:right]
                if left == 0:
                    right += 2
                else:
                    left -= 1
                    right += 1
            else:
                left += 1
                right += 1
        return ans
    def longestPalindrome(self, s: str) -> str:
        ans1, ans2 = Solution.expand(s, 0, 2), Solution.expand(s, 0, 3)
        if not ans1 and not ans2:
            return s[0]
        else:
            if len(ans1) > len(ans2):
                return ans1
            else:
                return ans2


sol = Solution()
s = "2345432"
print(sol.longestPalindrome(s))
