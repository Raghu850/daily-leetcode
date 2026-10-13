# class Solution:
#     def closeStrings(self, word1: str, word2: str) -> bool:
#         from collections import Counter
#         dict1, dict2 = dict(sorted(Counter(word1).items())), dict(sorted(Counter(word2).items()))
#         # print(sorted(dict1.values()), sorted(dict2.values()))
#         return sorted(dict1.values()) == sorted(dict2.values())
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter
        if set(word1) != set(word2): return False
        return sorted(Counter(word1).values()) == sorted(Counter(word2).values())