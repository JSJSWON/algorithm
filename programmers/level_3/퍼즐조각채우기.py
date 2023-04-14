# table에서 각 모양을 좌표로 따놓고(회전한 모양도 포함해서) game_board를 dfs로 탐색하면서 각 모양과 비교하면 되겠네
from copy import deepcopy

def solution(game_board, table):
    # table에서 각 모양의 좌표 구하기
    def get_crd_in_table(table, empty):  # empty == 0: 채워진 블록 찾기, empty == 1: 빈 블록 찾기
        path = []
        total_path = []

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(table) or j >= len(table[0]) or table[i][j] == empty or table[i][j] == -1:
                return
            table[i][j] = -1
            path.append([i, j])
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i, j + 1)

        for i in range(len(table)):
            for j in range(len(table[0])):
                if table[i][j] != empty:
                    dfs(i, j)
                    total_path.append(path)
                    path = []

        return total_path

    # game_board에서 구해주기
    g_paths = get_crd_in_table(game_board, 1)

    # paths와 g_paths에서 겹치는 모양 찾기

    def cnt():
        ans = 0
        visited = []
        while True:
            tmp = 0
            for g in deepcopy(g_paths):
                if g in visited:
                    continue
                for t in deepcopy(paths):
                    if len(g) == len(t):
                        if len(set([(g[i][0] - t[i][0], g[i][1] - t[i][1]) for i in range(len(g))])) == 1:
                            ans += len(g)
                            g_paths.remove(g)
                            for ii, jj in t:
                                table[ii][jj] = 0
                            paths.remove(t)
                            tmp = 1
                            break
                if tmp == 0:
                    visited.append(g)
                if tmp == 1:
                    break
            if tmp == 0:
                break
        return ans

    answer = 0
    paths = get_crd_in_table(deepcopy(table), 0)
    answer += cnt()
    table = list(map(list, zip(*reversed(table))))
    paths = get_crd_in_table(deepcopy(table), 0)
    answer += cnt()
    table = list(map(list, zip(*reversed(table))))
    paths = get_crd_in_table(deepcopy(table), 0)
    answer += cnt()
    table = list(map(list, zip(*reversed(table))))
    paths = get_crd_in_table(deepcopy(table), 0)
    answer += cnt()

    return answer
