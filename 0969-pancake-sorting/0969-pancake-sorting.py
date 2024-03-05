class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # copy array
        copy_arr = [num for num in arr]
        # sort the copied array using count sorting method
        max_range = max(copy_arr) + 1
        count = [0] * max_range
        for num in copy_arr:
            count[num] += 1
        target = 0
        for index, value in enumerate(count):
            for _ in range(value):
                copy_arr[target] = index
                target += 1
        res = []
        if copy_arr == arr:
            return res
        else:
            i = len(copy_arr) - 1
            while copy_arr != arr:
                index = arr.index(copy_arr[i])
                arr = arr[:index + 1][::-1] + arr[index + 1:]
                arr = arr[:i + 1][::-1] + arr[i + 1:]
                res.extend([index + 1, i + 1])
                i -= 1
        return res
