if __name__ == '__main__':
    score_pair = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_pair.append([name, score])
        scores.append(score)
    score_pair.sort(key=lambda x: x[1])
    scores = set(scores)
    scores = sorted(list(scores))
    second_score = scores[1]
    result = [pair for pair in score_pair if pair[1] == second_score]
    result.sort()
    for pair in result:
        print(pair[0])
