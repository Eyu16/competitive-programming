class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = 0
        p = 0
        leng = 0
        f_map = defaultdict(int)
        while r < len(nums):
            if nums[r] == 1:
                f_map[1] += 1
                r += 1
            else:
                f_map[0] += 1
                if f_map[0] == 2:
                    leng = max(leng, f_map[1])
                    if nums[p] == 0 and l != p:
                        f_map[1] -=(l - p - 1)
                    else:
                        f_map[1] -= (l - p)
                    f_map[0] -= 1
                    p = l
                    l = r
                else:
                    l = r
                r += 1

        if l == 0:
            return len(nums) - 1
        else:
            if nums[p] == 0:
                return max(leng, r - p - 2)
            else:
                return max(leng, r - p - 1)