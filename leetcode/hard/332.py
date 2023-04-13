from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for t in sorted(tickets):
            graph[t[0]].append(t[1])

        path = []

        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            path.append(a)  # 깊어질 때가 아닌 얕아질 때(답의 역순) 추가

        dfs('JFK')
        return path[::-1]


sol = Solution()
tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
print(sol.findItinerary(tickets))
