import math

def friend_recommendation(matrix, friend_matrix, target, U, I, K):
    similarity_list = []

    for u in range(U):
        if u != target and not friend_matrix[target][u]:
            dot = 0
            normA = 0
            normB = 0

            for i in range(I):
                dot += matrix[target][i] * matrix[u][i]
                normA += matrix[target][i] * matrix[target][i]
                normB += matrix[u][i] * matrix[u][i]

            if normA != 0 and normB != 0:
                similarity = dot / (math.sqrt(normA) * math.sqrt(normB))
            else:
                similarity = 0

            similarity_list.append((u, similarity))

    similarity_list.sort(key=lambda x: x[1], reverse=True)

    similar_users = []
    for i in range(K):
        similar_users.append(similarity_list[i][0])

    recommendation = [0] * I

    for u in similar_users:
        for i in range(I):
            if matrix[target][i] == 0:
                recommendation[i] += matrix[u][i]

    return similar_users, recommendation


matrix = [
    [1, 0, 1, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0],
    [1, 0, 0, 1, 1]
]

friend_matrix = [
    [False, True, False, False],
    [True, False, True, False],
    [False, True, False, True],
    [False, False, True, False]
]

users, rec = friend_recommendation(matrix, friend_matrix, 0, 4, 5, 2)

print("Similar Users:", users)
print("Recommendation:", rec)