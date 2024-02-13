class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result1 = []
        result2 = []
        frequency_map = {}
        for num in arr1:
            if num in frequency_map:
                frequency_map[num] += 1
            else:
                frequency_map[num] = 1
        for num in arr2:
            if num in frequency_map:
                result1.extend([num] * frequency_map[num])

        for num in arr1:
            if num not in arr2:
                result2.append(num)

        return result1 + sorted(result2)
        