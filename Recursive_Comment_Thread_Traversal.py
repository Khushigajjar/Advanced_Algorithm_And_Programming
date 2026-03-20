from datetime import datetime
from tkinter import END
class CommentNode:
    def __init__(self, comment_id, user_id, content, timestamp, likes):
        self.comment_id = comment_id
        self.user_id = user_id
        self.content = content
        self.timestamp = timestamp
        self.likes = likes
        self.replies = []

def display_thread(comment, level=0):
    indentation = "  " * level
    print(f"{indentation}{comment.content} (ID: {comment.comment_id}, User: {comment.user_id})")
    for reply in comment.replies:
        display_thread(reply, level + 1)

def count_total_comments(comment):
    total_comments = 1
    for reply in comment.replies:
        total_comments += count_total_comments(reply)
    return total_comments

def total_likes(comment):
    total = comment.likes
    for reply in comment.replies:
        total += total_likes(reply)
    return total

def find_deepest_reply(comment):
    if not comment.replies:
        return 0
    max_depth = 0
    for reply in comment.replies:
        depth = find_deepest_reply(reply)
        if depth > max_depth:
            max_depth = depth
    return max_depth + 1


def search_by_user(user_id, comment):
    result = []
    if comment.user_id == user_id:
        result.append(comment)
    for reply in comment.replies:
        result.extend(search_by_user(user_id, reply))
    return result

def contains_keyword(keyword, comment):
    if keyword in comment.content:
        return True
    for reply in comment.replies:
        if contains_keyword(keyword, reply):
            return True
    return False


def delete_comment(comment_id, thread):
    new_thread = []
    for comment in thread:
        if comment.comment_id != comment_id:
            comment.replies = delete_comment(comment_id, comment.replies)
            new_thread.append(comment)
    return new_thread


c101 = CommentNode(101, "Alice", "This recipe looks amazing!", datetime.now(), 5)
c201 = CommentNode(201, "Bob", "I tried it last night!", datetime.now(), 3)
c202 = CommentNode(202, "Charlie", "Can I use olive oil instead?", datetime.now(), 2)
c301 = CommentNode(301, "Alice", "What did you think?", datetime.now(), 4)
c302 = CommentNode(302, "Alice", "Yes, that works too!", datetime.now(), 1)
c401 = CommentNode(401, "Bob", "It was delicious!", datetime.now(), 6)

c101.replies = [c201, c202]
c201.replies = [c301]
c301.replies = [c401]
c202.replies = [c302]

print("DISPLAY THREAD:")
display_thread(c101)

print("\nTOTAL COMMENTS:", count_total_comments(c101))
print("TOTAL LIKES:", total_likes(c101))
print("DEEPEST LEVEL:", find_deepest_reply(c101))

print("\nSEARCH BY USER (Alice):")
results = search_by_user("Alice", c101)
for r in results:
    print(r.content)

print("\nCONTAINS 'olive':", contains_keyword("olive", c101))

thread = [c101]
thread = delete_comment(201, thread)

print("\nTHREAD AFTER DELETION:")
display_thread(thread[0])