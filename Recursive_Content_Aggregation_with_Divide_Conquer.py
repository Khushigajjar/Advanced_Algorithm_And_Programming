from datetime import datetime

class Post:
	def __init__(self, post_id, user_id, content_preview, timestamp, likes, comments, shares):
		self.post_id = post_id
		self.user_id = user_id
		self.content_preview = content_preview
		self.timestamp = timestamp
		self.likes = likes
		self.comments = comments
		self.shares = shares
		self.engagement_score = (likes * 1) + (comments * 2) + (shares * 3)


def max_engagement(posts, left, right):
	if left == right:
		return posts[left].engagement_score

	mid = (left + right) // 2
	left_max = max_engagement(posts, left, mid)
	right_max = max_engagement(posts, mid + 1, right)

	if left_max >= right_max:
		return left_max
	return right_max


def sum_engagement(posts, left, right):
	if left == right:
		return posts[left].engagement_score

	mid = (left + right) // 2
	return sum_engagement(posts, left, mid) + sum_engagement(posts, mid + 1, right)


def average_engagement(posts, left, right):
	total = sum_engagement(posts, left, right)
	n = right - left + 1
	return total / n


def count_above_threshold(posts, left, right, threshold):
	if left == right:
		if posts[left].engagement_score > threshold:
			return 1
		return 0

	mid = (left + right) // 2
	return (
		count_above_threshold(posts, left, mid, threshold)
		+ count_above_threshold(posts, mid + 1, right, threshold)
	)


def merge_sort_by_engagement(posts, left, right):
	if left >= right:
		return

	mid = (left + right) // 2
	merge_sort_by_engagement(posts, left, mid)
	merge_sort_by_engagement(posts, mid + 1, right)
	merge(posts, left, mid, right)


def merge(posts, left, mid, right):
	left_part = posts[left : mid + 1]
	right_part = posts[mid + 1 : right + 1]

	i = 0
	j = 0
	k = left

	while i < len(left_part) and j < len(right_part):
		if left_part[i].engagement_score >= right_part[j].engagement_score:
			posts[k] = left_part[i]
			i += 1
		else:
			posts[k] = right_part[j]
			j += 1
		k += 1

	while i < len(left_part):
		posts[k] = left_part[i]
		i += 1
		k += 1

	while j < len(right_part):
		posts[k] = right_part[j]
		j += 1
		k += 1


def find_peak_hour(likes, left, right):
	if left == right:
		return left

	mid = (left + right) // 2
	if likes[mid] >= likes[mid + 1]:
		return find_peak_hour(likes, left, mid)
	return find_peak_hour(likes, mid + 1, right)


def display_posts(posts):
	for post in posts:
		print(
			f"Post {post.post_id} | User: {post.user_id} | "
			f"Score: {post.engagement_score} | Preview: {post.content_preview}"
		)


p1 = Post(1, "Aarav", "Street chess finals at city library", datetime.now(), 27, 8, 6)
p2 = Post(2, "Meera", "Midnight meteor shower timelapse", datetime.now(), 41, 12, 9)
p3 = Post(3, "Kabir", "Grandma's mango pickle batch is ready", datetime.now(), 19, 11, 4)
p4 = Post(4, "Nisha", "Cycle trip from Pune to Goa highlights", datetime.now(), 36, 10, 8)
p5 = Post(5, "Rohan", "Campus food fest secret menu reveal", datetime.now(), 24, 14, 5)
p6 = Post(6, "Ira", "First rain chai stall live acoustic set", datetime.now(), 33, 9, 7)

posts = [p1, p2, p3, p4, p5, p6]

left = 0
right = len(posts) - 1

print("POSTS BEFORE SORT:")
display_posts(posts)

print("\nMAX ENGAGEMENT SCORE:", max_engagement(posts, left, right))

total = sum_engagement(posts, left, right)
avg = average_engagement(posts, left, right)
print("TOTAL ENGAGEMENT SCORE:", total)
print("AVERAGE ENGAGEMENT SCORE:", round(avg, 2))

threshold = 55
count = count_above_threshold(posts, left, right, threshold)
print(f"POSTS WITH SCORE > {threshold}:", count)

merge_sort_by_engagement(posts, left, right)
print("\nPOSTS AFTER MERGE SORT (HIGH TO LOW):")
display_posts(posts)

hourly_likes = [
	2,
	3,
	3,
	5,
	8,
	13,
	21,
	34,
	55,
	73,
	96,
	120,
	147,
	162,
	171,
	164,
	149,
	130,
	108,
	82,
	59,
	37,
	18,
	9,
]

peak_hour = find_peak_hour(hourly_likes, 0, len(hourly_likes) - 1)
print(f"\nPEAK HOUR INDEX: {peak_hour} (Likes: {hourly_likes[peak_hour]})")
