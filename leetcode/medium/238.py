from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left, right = [1], [1]
        # left, right 둘 다 만들 필요가 없음. 하나만 만들고 연산으로 처리하면 메모리가 절약되겠지. -> 기존 변수 재활용
        # 참고) 출력에 필요한 공간은 공간 복잡도에 포함하지 않는다.
        ans = [1]
        for i in range(len(nums) - 1):
            ans.append(ans[-1] * nums[i])
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= p
            p *= nums[i]
        return ans

sol = Solution()
nums = [1,2,3,4]
print(sol.productExceptSelf(nums))
