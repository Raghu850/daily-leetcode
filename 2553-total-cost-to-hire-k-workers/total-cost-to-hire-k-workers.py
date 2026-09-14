class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        costLen = len(costs)
        left = candidates
        right = costLen - 1 - candidates

        minHeapLeft = costs[:candidates]
        minHeapRight = costs[max(candidates, costLen - candidates):]

        heapq.heapify(minHeapLeft)
        heapq.heapify(minHeapRight)

        total = 0

        for _ in range(k):
            if not minHeapRight or (minHeapLeft and minHeapLeft[0] <= minHeapRight[0]):
                if left <= right:
                    total += heapq.heapreplace(minHeapLeft, costs[left])
                    left += 1
                else:
                    total += heapq.heappop(minHeapLeft)
            else:
                if left <= right:
                    total += heapq.heapreplace(minHeapRight, costs[right])
                    right -= 1
                else:
                    total += heapq.heappop(minHeapRight)

        return total