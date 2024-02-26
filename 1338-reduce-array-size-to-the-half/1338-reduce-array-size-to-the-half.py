class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count_f = Counter(arr)
        n = int(len(arr) / 2)
        sums = 0
        nums = []
        loop_over = [[key, count_f[key]] for key in count_f]
        loop_over.sort(key=lambda x: x[1])
        for i in range(len(loop_over)-1, -1, -1):
            if loop_over[i][1] >= n:
                return 1
            elif sums < n:
                sums += loop_over[i][1]
                nums.append(loop_over[i][0])
            else:
                return len(nums)
        return 0