class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        map = defaultdict(int)

        i = 0
        j = 0
        l = 0

        while j < len(fruits) and i < len(fruits):
            map[fruits[j]] += 1
            if len(map) > 2:
                l = max(l, j - i)
                map[fruits[i]] -= 1
                if map[fruits[i]] == 0:
                    del map[fruits[i]]
                i += 1
                map[fruits[j]] -= 1
            else:
                j += 1

        l = max(l, j - i)
        return l