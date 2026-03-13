# Advanced Algorithm and Programming Exercises

## Team Members
- Khushi Gajjar (Exercise-1,2)
- Rahul Kumar Reddy Duggempudi (Exercise-3,4)

## Exercise 2: Activity Feed Processing with Stacks and Queues

### Objective
Implement stack and queue operations to manage activities and notifications in a social app style system.

### What I implemented

#### Part A: Recent Activity Stack
- `ActivityNode`
- `ActivityStack`
- `push`, `pop`, `peek`, `is_empty`, `size`, `display_recent`
- `undo_last(activity_stack, undo_stack)`

#### Part B: Notification Queue
- `NotificationNode`
- `NotificationQueue`
- `enqueue`, `dequeue`, `front`, `is_empty`, `size`
- `priority_enqueue(queue, notification)`

#### Part C: Integrated Feed Processing
- `FeedProcessor`
- `process_incoming(system)`
- `batch_process(system, k)`
- `clear_history(system)`
- `get_stats(system)`

### Test Cases
| Test Case | Operation | Expected Output |
|---|---|---|
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

### Time Complexity
- Stack operations (`push`, `pop`, `peek`, `is_empty`, `size`): `O(1)`
- Queue operations (`enqueue`, `dequeue`, `front`, `is_empty`, `size`): `O(1)`
- `batch_process(k)`: `O(k)`
- `clear_history(r)`: `O(r)`

### Run
```bash
python Exercise2_Activity_Feed_Processing.py
```
