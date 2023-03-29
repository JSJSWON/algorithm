from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)
        for s in strs:
            # str_dict[tuple(sorted(s))].append(s)
            str_dict[''.join(sorted(s))].append(s)
        return list(str_dict.values())


sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagrams(strs))


######################################################################
from sys import getsizeof

word = 'zz'
str_ = word
tuple_ = tuple(word)

print(getsizeof(str_))
print(getsizeof(tuple_))
# 메모리 사이즈
# 한 글자일 때: string > tuple
# 나머지: string < tuple
######################################################################
