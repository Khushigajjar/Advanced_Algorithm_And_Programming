def social_analysis(friend_matrix, target, U):
    mutual_pairs = []

    for i in range(U):
        for j in range(i + 1, U):
            if friend_matrix[i][j] and friend_matrix[j][i]:
                mutual_pairs.append((i, j))

    followers = 0
    following = 0

    for i in range(U):
        if friend_matrix[i][target]:
            followers += 1
        if friend_matrix[target][i]:
            following += 1

    influence = (followers + following) / U

    return mutual_pairs, influence


friend_matrix = [
    [False, True, False, False],
    [True, False, True, False],
    [False, True, False, True],
    [False, False, True, False]
]

pairs, score = social_analysis(friend_matrix, 0, 4)

print("Mutual Pairs:", pairs)
print("Influence Score:", score)