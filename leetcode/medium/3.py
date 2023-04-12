from collections import deque, defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = deque()  # 책에서는 queue를 사용하지 않고 투 포인터를 사용함
        count = defaultdict(int)
        m, ans = 0, 0

        for string in s:
            while count[string] != 0:
                tmp = queue.popleft()
                count[tmp] -= 1
                m -= 1

            queue.append(string)
            count[string] += 1
            m += 1
            ans = max(ans, m)

        return ans


sol = Solution()
s = 'pwwkew'
print(sol.lengthOfLongestSubstring(s))
