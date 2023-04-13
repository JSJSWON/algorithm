from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(csum, index, path):
            if csum < 0:
                return  # 탐색 종료(가지 치기)
            if csum == 0:
                result.append(path)
                return  # 탐색 종료(가지 치기)
            for i in range(index, len(candidates)):
                # dfs 함수에 i가 들어감으로써 자기 자신을 포함해 뒤에 있는 숫자들을 탐색할 수 있음
                # 이로 인해 candidates[i] == 0이면 무한히 깊이 탐색을 하게 됨(테스트 케이스에는 0이 없지만)
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result


sol = Solution()
candidates = [2, 3, 6, 7]
target = 7
print(sol.combinationSum(candidates, target))
