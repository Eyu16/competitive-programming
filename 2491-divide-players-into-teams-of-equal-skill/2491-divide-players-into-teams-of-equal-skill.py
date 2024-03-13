class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        res = 0
        sum_set = set()
        skill.sort()
        i = 0
        j = len(skill) - 1
        while i < j:
            sums = skill[i] + skill[j]
            sum_set.add(sums)
            if len(sum_set) == 0 or len(sum_set) == 1:
                res += (skill[i] * skill[j])
                i += 1
                j -= 1
            else:
                return -1

        return res