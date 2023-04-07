from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        count = Counter(stones)
        for jewel in jewels:
            ans += count[jewel]
        return ans


sol = Solution()
jewels = "aA"
stones = "aAAbbbb"
print(sol.numJewelsInStones(jewels, stones))
