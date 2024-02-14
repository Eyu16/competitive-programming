class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        check = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                check.add(fronts[i])
        result = float("inf")
        for num in (fronts + backs):
            if num not in check:
                result = min(result, num)
        return result if result != float("inf") else 0