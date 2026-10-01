class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        # sort first then do two pointer
        products.sort()

        result = []
        left = 0
        right = len(products) - 1

        for i, c in enumerate(searchWord):
            while left <= right and( len(products[left]) <= i or c != products[left][i]):
                left += 1

            while left <= right and( len(products[right]) <= i or c != products[right][i]):
                right -= 1

            path = []
            for index in range(left, min(left +3, right + 1)):
                path.append(products[index])
            result.append(path)
        return result