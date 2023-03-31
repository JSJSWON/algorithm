from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 10 ** 4 # 하나의 화살표만 두기(두 개를 사용할 때 for loop이 중복되면 하나로 합치기)
        profit = 0
        for price in prices:
            if price < low:
                low = price
            profit = max(profit, price - low)
        return profit


sol = Solution()
prices = [5,4,3,2,1]
print(sol.maxProfit(prices))
