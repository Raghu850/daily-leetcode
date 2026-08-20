class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        v1 = c1.values()
        v2 = c2.values()
        k1 = c1.keys()
        k2 = c2.keys()
        if sorted(k1) != sorted(k2):
            return False
        for val1, val2 in zip(sorted(v1), sorted(v2)):
            if val1 != val2:
                return False
        return True