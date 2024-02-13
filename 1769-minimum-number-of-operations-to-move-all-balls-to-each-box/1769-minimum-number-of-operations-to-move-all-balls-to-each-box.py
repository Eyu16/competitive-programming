class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ball_address = []
        result = []
        for i in range(len(boxes)):
            if boxes[i] == '1':
                ball_address.append(i)

        for i in range(len(boxes)):
            moves = 0
            for j in ball_address:
                moves += abs(j - i)
            result.append(moves)
        return result
