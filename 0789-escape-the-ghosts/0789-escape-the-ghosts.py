class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        person_distance = abs(target[0]) + abs(target[1])
        ghosts_distance = [abs(target[0] - ghost[0]) + abs(target[1] - ghost[1]) for ghost in ghosts]
        if person_distance < min(ghosts_distance):
            return True
        return False
