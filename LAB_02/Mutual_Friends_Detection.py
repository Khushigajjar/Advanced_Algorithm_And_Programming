FUNCTION mutual_friends(setA, setB):
    RETURN setA ∩ setB   

FUNCTION unique_friends(setA, setB):
    RETURN setA - setB   

FUNCTION all_friends(setA, setB):
    RETURN setA ∪ setB   

FUNCTION jaccard_similarity(setA, setB):
    intersection_size ← SIZE(mutual_friends(setA, setB))
    union_size ← SIZE(all_friends(setA, setB))
    IF union_size > 0 THEN
        RETURN intersection_size / union_size
    ELSE
        RETURN 0
    END IF

FUNCTION friend_suggestions(user_set, all_friend_sets):
    suggestions ← EMPTY_SET

    FOR each friend IN user_set DO
        friends_of_friend ← all_friend_sets[friend]   
        FOR each f IN friends_of_friend DO
            IF f NOT IN user_set AND f ≠ user_id THEN
                ADD f TO suggestions
            END IF
        END FOR
    END FOR

    RETURN suggestions



