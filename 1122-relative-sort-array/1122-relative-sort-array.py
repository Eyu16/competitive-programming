class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result1 = []
        result2 = []
        for num1 in arr2:
            for num2 in arr1:
                if num2 == num1 and num2 in arr2:
                    result1.append(num2)
        for num in arr1:
            if num not in arr2:
                result2.append(num)
        return result1 + sorted(result2)
        