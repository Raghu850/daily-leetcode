class Solution:
    def suggestedProducts(self, prods: List[str], word: str) -> List[List[str]]:
        prods.sort()

        prefix: str = ""
        ans: list[list[str]] = []

        for i in range(0, len(word)):
            prefix += word[i]
            top_3_prods: list[str] = self.search_top_3(prefix, prods)
            ans.append(top_3_prods)

        return ans

    # mobile, moneypot, monitor, mouse, mousepad
    def search_top_3(self, prefix: str, prods: list[str]) -> list[str]:
        start: int = 0
        end: int = len(prods) - 1
        idx: int = 0

        while start <= end:
            mid: int = start + (end - start) // 2

            mid_prefix: str = prods[mid][0: len(prefix)]
            if mid_prefix >= prefix:
                idx = mid
                end = mid - 1
            elif mid_prefix < prefix:
                start = mid + 1

        common_prefixs: list[str] = []
        cnt: int = 0
        while idx < len(prods) and cnt < 3:
            if prefix == prods[idx][0: len(prefix)]:
                common_prefixs.append(prods[idx])
            else:
                break

            cnt += 1
            idx += 1

        return common_prefixs