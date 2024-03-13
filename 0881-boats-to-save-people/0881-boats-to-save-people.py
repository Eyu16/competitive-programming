class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people) == 1:
            if people[0] <= limit:
                return 1
        boats = 0
        i = 0
        j = len(people) - 1
        people.sort()
        while i <= j:
            if people[i] + people[j] <= limit:
                boats += 1
                i += 1
                j -= 1
            else:
                boats += 1
                j -= 1

        return boats

        