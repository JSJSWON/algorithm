from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []

        def dfs(cursor, comb):
            if len(comb) == k:
                answer.append(comb[:])  # 여기서 그냥 comb를 append 해버리면 comb에 대한 참조가 추가됨
                # 참조된 값이 변경될 때 answer에 있는 값도 함께 변경되는 것을 막으려면 값을 복사해서 넣어줘야 함

            for i in range(cursor, n):
                comb.append(i + 1)
                dfs(cursor + 1, comb)
                comb.pop()
                cursor += 1

        dfs(0, [])

        return answer


sol = Solution()
n = 5
k = 4
print(sol.combine(n, k))
