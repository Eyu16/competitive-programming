class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list2_map = {i: value for value, i in enumerate(list2)}
        sums = []
        result = []
        for i, value in enumerate(list1):
            if value in list2_map:
                sums.append([value, list2_map[value] + i])
        sums.sort(key=lambda x: x[1])
        min = sums[0][1]
        for i in range(len(sums)):
            if sums[i][1] == min:
                result.append(sums[i][0])

        return result
        