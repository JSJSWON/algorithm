from typing import List
from collections import Counter
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'\W', ' ', paragraph)
        sep = paragraph.lower().split()
        return Counter(x for x in sep if x not in banned).most_common(1)[0][0]


sol = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(sol.mostCommonWord(paragraph, banned))
