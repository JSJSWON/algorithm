from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []
        for log in logs:
            if log.split()[1].isnumeric():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        return sorted(letter_logs, key=lambda x: (x.split()[1:], x.split()[0])) + digit_logs


sol = Solution()
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
sol.reorderLogFiles(logs)
