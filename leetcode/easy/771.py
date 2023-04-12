from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        count = Counter(stones)  # Counter는 존재하지 않는 키에 대해 에러를 발생하는 게 아니라 0을 출력해 줌
        for jewel in jewels:
            ans += count[jewel]
        return ans

        # 한 줄 답
        # return sum(stone in jewels for stone in stones)


sol = Solution()
jewels = "aA"
stones = "aAAbbbb"
print(sol.numJewelsInStones(jewels, stones))
