class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        initial = capacity
        steps = 0
        for i in range(len(plants)):
            if capacity >= plants[i]:
                capacity -= plants[i]
                steps += 1
            else:
                capacity = initial - plants[i]
                steps = steps + (2 * i) + 1

        return steps
        