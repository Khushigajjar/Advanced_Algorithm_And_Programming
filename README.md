# Advanced Algorithm and Programming Exercises

## Team Members
1. **Khushi Gajjar** – Exercise 1  
2. **Rahul Kumar Reddy Duggempudi** – Exercise 2  
3. **ZiJie HUANG** – Exercise 3  

---

# Exercise 1: Content Feed Navigation with Doubly Linked List

## Objective
This exercise implements a **story feed system** using a **doubly linked list (DLL)**. Each story is represented as a node with `content`, `story_id`, and a `views` counter. The doubly linked list allows **bidirectional navigation**, insertion, deletion, and reordering of stories based on views. The exercise demonstrates how DLLs can efficiently support operations like moving forward/backward, jumping to a story, tracking views, and displaying nearby stories.

---

## Time Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|----------------|
| `add_story` | O(1) | O(1) |
| `remove_story` | O(n) | O(1) |
| `move_forward` | O(1) | O(1) |
| `move_backward` | O(1) | O(1) |
| `jump_to` | O(n) | O(1) |
| `insert_after` | O(n) | O(1) |
| `display_around_current(k)` | O(k) | O(1) |
| `track_view` | O(1) | O(1) |
| `most_viewed` | O(n) | O(1) |
| `reorder_by_views` | O(n²) | O(n) |
| `display` | O(n) | O(1) |

---

## Notes on Forward vs. Backward Navigation
- Forward navigation is **O(1)** in both singly and doubly linked lists.  
- Backward navigation is **O(n)** in singly linked lists (must rescan from head), but **O(1)** in doubly linked lists using the `prev` pointer.  
- Removing a node by pointer is **O(n)** in singly linked lists but **O(1)** in doubly linked lists.  
- Doubly linked lists require **8 extra bytes per node** for the `prev` pointer.

---

## Conclusion
Doubly linked lists are ideal for applications like story feeds, browser history, or playlists where **bidirectional navigation** and **fast node deletion** are needed. The small memory overhead is justified by the advantage of **O(1) backward traversal** and **O(1) removal given a pointer**, making DLLs more efficient than singly linked lists for these use cases.

---

# Exercise 2: Activity Feed Processing with Stacks and Queues

## Objective
Implement stack and queue operations to manage activities and notifications in a social app style system.

## Implemented Features

### Part A: Recent Activity Stack
- `ActivityNode` and `ActivityStack`  
- Operations: `push`, `pop`, `peek`, `is_empty`, `size`, `display_recent`  
- `undo_last(activity_stack, undo_stack)`  

### Part B: Notification Queue
- `NotificationNode` and `NotificationQueue`  
- Operations: `enqueue`, `dequeue`, `front`, `is_empty`, `size`  
- `priority_enqueue(queue, notification)`  

### Part C: Integrated Feed Processing
- `FeedProcessor`  
- Operations: `process_incoming(system)`, `batch_process(system, k)`, `clear_history(system)`, `get_stats(system)`  

---

## Test Cases

| Test Case | Operation | Expected Output |
|-----------|-----------|----------------|
| TC1 | Push 4 activities, then `peek(activity_stack)` | `Updated profile` |
| TC2 | `size(activity_stack)` after 4 pushes | `4` |
| TC3 | `display_recent(activity_stack, 3)` | `Updated profile`, `Shared a reel`, `Commented on a photo` |
| TC4 | `undo_last(activity_stack, undo_stack)` | Return: `Updated profile` |
| TC5 | After undo, `peek(activity_stack)` and `peek(undo_stack)` | `Shared a reel`, `Updated profile` |
| TC6 | Enqueue 3 notifications + `priority_enqueue(...)`, then `front(queue)` | `Urgent: Account security alert` |
| TC7 | Dequeue twice from queue | `Urgent: Account security alert`, `Friend request from Alex` |
| TC8 | Before processing, `get_stats(system)` | `(0, 3, 0)` |
| TC9 | After `batch_process(system, 2)`, `get_stats(system)` | `(2, 1, 0)` |
| TC10 | After `clear_history(system)`, `get_stats(system)` | `(0, 1, 2)` |

---

## Time Complexity
- **Stack operations** (`push`, `pop`, `peek`, `is_empty`, `size`) → O(1)  
- **Queue operations** (`enqueue`, `dequeue`, `front`, `is_empty`, `size`) → O(1)  

---

# Exercise 3: Post Ranking using Priority Queue

## Objective
Implement a **priority queue system** to rank social media posts based on engagement scores. The system simulates how social media platforms prioritize content in a feed according to user interactions.

---

## Data Model
Each post contains:  
- `postId` – unique identifier  
- `userId` – ID of the user who created the post  
- `content` – text content  
- `timestamp` – creation time  
- `likes`, `comments`, `shares`  
- `engagementScore` = `likes * 1 + comments * 2 + shares * 3`  

---

## Priority Queue Implementation
- Sorted **singly linked list**, posts stored in descending order of engagement score  
- Operations:  
  1. `enqueue(post)` – insert while maintaining order  
  2. `peekMax()` – return highest score post  
  3. `dequeueMax()` – remove and return highest score post  
  4. `updateScore(postId, likes, comments, shares)` – update engagement and reposition  
  5. `getTopK(k)` – retrieve top K posts  
  6. `decayOlderThan(timestamp)` – reduce older posts by 20% and refresh ordering  

---

## Example Execution
- **Initial queue:** `[Post3: 95] -> [Post1: 82] -> [Post2: 47] -> [Post4: 23]`  
- **Peek max:** `[Post3: 95]`  
- **Update Post2 score:** `[Post3: 95] -> [Post1: 82] -> [Post2: 57] -> [Post4: 23]`  
- **Top 3 posts:** `[Post3: 95]`, `[Post1: 82]`, `[Post2: 57]`  
- **Apply decay (>30 min old):** `[Post1: 82] -> [Post3: 74] -> [Post2: 57] -> [Post4: 23]`  
- **Dequeue max:** `[Post1: 82]`  
- **Queue size:** 3  

---

## Time Complexity

| Operation | Time Complexity |
|-----------|----------------|
| `enqueue` | O(n) |
| `peekMax` | O(1) |
| `dequeueMax` | O(1) |
| `updateScore` | O(n) |
| `getTopK` | O(k) |
| `decayOlderThan` | O(n) |

> Since the priority queue is implemented using a sorted linked list, insertion and updates require traversal of the list.

---

## Conclusion
This exercise demonstrates how a priority queue can dynamically rank posts in a social media feed based on engagement metrics. By combining engagement scoring, dynamic updates, and time-based decay, the system simulates a simplified version of real-world content ranking algorithms used by modern social media platforms.
