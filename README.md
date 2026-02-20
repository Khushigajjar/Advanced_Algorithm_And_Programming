# Advanced Algorithm and Programming Exercises

## Team Members
- Khushi Gajjar (Excercise-1,2)
- Rahul Kumar Reddy Duggempudi (Excecise-3,4)
---

## Exercise 1: Message Classification

### Objective
Analyze a textual message and classify it as **CALM**, **URGENT**, or **AGGRESSIVE** based on:
- Uppercase letters ratio  
- Punctuation marks  
- Repeated characters (spam detection)  

### Algorithm
1. Count uppercase letters, punctuation marks, and alphabetic characters.  
2. Detect repeated characters (more than 3 in sequence).  
3. Compute caps ratio: `uppercase_count / alphabetic_count`.  
4. Classify messages:
   - `AGGRESSIVE` → caps ratio ≥ 0.6 or punctuation ≥ 5  
   - `URGENT` → caps ratio ≥ 0.3 or punctuation ≥ 3  
   - `CALM` → otherwise  

### Test Cases

| Message                             | Uppercase | Punctuation | Caps Ratio | Classification |
|------------------------------------|-----------|-------------|------------|----------------|
| "Hey, want to connect?"             | 1         | 1           | 0.11       | CALM           |
| "PLEASE ACCEPT MY REQUEST!!!"       | 3         | 3           | 1.0        | AGGRESSIVE     |
| "Are you free? I need to talk!!!"  | 1         | 4           | 0.08       | URGENT         |

### Complexity
- **Time:** O(n), n = length of message  
- **Space:** O(1), only counters and flags  

---

## Exercise 2: Mutual Friends Detection

### Objective
Detect social connections between users:
1. Mutual friends – people both users know  
2. Unique friends – friends unique to each user  
3. Friend-of-friend suggestions – second-degree connections not already connected  
4. Jaccard similarity – intersection size / union size of friend sets  

### Algorithm
- Represent each user's friends as a set.  
- Perform set operations:
  - `&` → mutual friends  
  - `-` → unique friends  
  - `|` → union of friends  
- For friend suggestions, iterate over each friend and their friends, add those not already in the user's set.  
- Compute Jaccard similarity between two users’ social circles.  

### Test Cases

| User A Friends         | User B Friends         | Mutual    | Unique A       | Unique B       | Jaccard Similarity |
|------------------------|----------------------|-----------|----------------|----------------|------------------|
| {101,102,103,104,105} | {103,104,106,107,108}| {103,104} | {101,102,105}  | {106,107,108}  | 0.25             |

| User ID | Suggestions (Friends-of-Friends) |
|---------|----------------------------------|
| 101     | {104,105}                        |

### Complexity
- **Hash Set:**  
  - Intersection & difference → O(min(m, n))  
  - Friend suggestions → O(F × average_friend_count)  
- **Sorted Array:** O(m + n)  
- **Bit Array:** O(N/W), N = max ID, W = CPU word size  

- **Space:** O(number of friends stored in sets)  


## Exercise 3: Friend Recommendation by Common Interests

### Objective
Recommend new friends and interests based on user behavior:
- Identify similar users using common interests  
- Recommend new interests using collaborative filtering  

---

### Algorithm
- Represent user interests using a matrix  
- For each user:
  - Compute similarity with the target user using cosine similarity  
- Select top K similar users  
- Recommend interests:
  - Add interests from similar users  
  - Ignore already existing interests of the target user  

---

### Test Cases

| Target User | Similar Users | Recommendation | Purpose |
|------------|--------------|---------------|--------|
| User 0 | [3, 2] | [0,1,0,2,0] | Normal case |
| All zeros | [] | [0,0,0,0,0] | No interests |
| Identical users | Any top K | Same pattern | Similarity check |
| K > U | Max users | Valid output | Boundary case |
| No non-friends | [] | [0,...] | No recommendation |

---

### Complexity

**Time Complexity**
- Pairwise similarity → O(U² × I)  
- Optimized (sparse data) → O(U² × k), where k ≪ I  

**Space Complexity**
- Interest matrix → O(U × I)  
- Recommendation array → O(I)  

---

## Exercise 4: Mutual Followers Matrix

### Objective
Analyze social network relationships:
- Identify mutual followers  
- Calculate influence score of a user  

---

### Algorithm
- Represent connections using adjacency matrix  
- For mutual followers:
  - Check if user i follows j AND j follows i  
- For influence score:
  - Count followers (incoming links)  
  - Count following (outgoing links)  
  - Compute:
    influence = (followers + following) / total users  

---

### Test Cases

| Friend Matrix Type | Mutual Pairs | Influence | Purpose |
|------------------|-------------|----------|--------|
| Sample matrix | [(0,1),(1,2),(2,3)] | 0.5 | Normal case |
| No connections | [] | 0 | No followers |
| Fully connected | All pairs | High value | Dense graph |
| One-sided follow | [] | Low | No mutual |
| Single user | [] | 0 | Edge case |

---

### Complexity

**Time Complexity**
- Mutual followers → O(U²)  
- Followers & following → O(U)  

**Space Complexity**
- Adjacency matrix → O(U²)  

---

