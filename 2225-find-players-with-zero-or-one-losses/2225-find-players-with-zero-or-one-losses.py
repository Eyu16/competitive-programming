class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = []
        losers = {}
        l_array = []
        for pair in matches:
            winners.append(pair[0])
            if pair[1] in losers:
                losers[pair[1]] += 1
            else:
                losers[pair[1]] = 1

        winners = list(set(winners))
        winners = [winner for winner in winners if winner not in losers]
        for loser in losers:
            if losers[loser] == 1:
                l_array.append(loser)

        return [sorted(winners), sorted(l_array)]
        
        