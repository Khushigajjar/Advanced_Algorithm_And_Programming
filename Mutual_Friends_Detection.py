def mutual_friends(setA, setB):
    return setA & setB

def unique_friends(setA, setB):
    return setA - setB

def all_friends(setA, setB):
    return setA | setB

def jaccard_similarity(setA, setB):
    intersection_size = len(mutual_friends(setA, setB))
    union_size = len(all_friends(setA, setB))
    if union_size > 0:
        return intersection_size / union_size
    else:
        return 0

def friend_suggestions(user_id, user_set, all_friend_sets):
    suggestions = set()
    for friend in user_set:
        friends_of_friend = all_friend_sets.get(friend, set())
        for f in friends_of_friend:
            if f not in user_set and f != user_id:
                suggestions.add(f)
    return suggestions

userA_friends = {101, 102, 103, 104, 105}
userB_friends = {103, 104, 106, 107, 108}

all_friend_sets = {
    101: {102, 103},
    102: {101, 104},
    103: {101, 104, 105},
    104: {102, 103},
    105: {103},
    106: {107, 108},
    107: {106},
    108: {106}
}

print("Mutual friends:", mutual_friends(userA_friends, userB_friends))
print("Unique to A:", unique_friends(userA_friends, userB_friends))
print("Unique to B:", unique_friends(userB_friends, userA_friends))
print("All friends:", all_friends(userA_friends, userB_friends))
print("Jaccard similarity:", jaccard_similarity(userA_friends, userB_friends))
print("Friend suggestions for 101:", friend_suggestions(101, userA_friends, all_friend_sets))