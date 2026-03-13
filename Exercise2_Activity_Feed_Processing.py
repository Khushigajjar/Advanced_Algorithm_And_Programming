class ActivityNode:
    def __init__(self, activity_type):
        self.activity_type = activity_type
        self.next = None


class ActivityStack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, activity):
        new_node = ActivityNode(activity)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.top is None:
            return "Stack Empty"
        temp = self.top
        self.top = self.top.next
        self._size -= 1
        return temp.activity_type

    def peek(self):
        if self.top is None:
            return "Stack Empty"
        return self.top.activity_type

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size

    def display_recent(self, n):
        current = self.top
        count = 0
        while current is not None and count < n:
            print(current.activity_type)
            current = current.next
            count += 1


def push(stack, activity):
    stack.push(activity)


def pop(stack):
    return stack.pop()


def peek(stack):
    return stack.peek()


def is_empty(ds):
    return ds.is_empty()


def size(ds):
    return ds.size()


def display_recent(stack, n):
    stack.display_recent(n)


def undo_last(activity_stack, undo_stack):
    last_activity = pop(activity_stack)
    if last_activity != "Stack Empty":
        push(undo_stack, last_activity)
    return last_activity


class NotificationNode:
    def __init__(self, notification):
        self.notification = notification
        self.next = None


class NotificationQueue:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def enqueue(self, notification):
        new_node = NotificationNode(notification)
        if self._rear is None:
            self._front = new_node
            self._rear = new_node
        else:
            self._rear.next = new_node
            self._rear = new_node
        self._size += 1

    def dequeue(self):
        if self._front is None:
            return "Queue Empty"
        temp = self._front
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1
        return temp.notification

    def front(self):
        if self._front is None:
            return "Queue Empty"
        return self._front.notification

    def is_empty(self):
        return self._front is None

    def size(self):
        return self._size

    def priority_enqueue(self, notification):
        new_node = NotificationNode(notification)
        new_node.next = self._front
        self._front = new_node
        if self._rear is None:
            self._rear = new_node
        self._size += 1


def enqueue(queue, notification):
    queue.enqueue(notification)


def dequeue(queue):
    return queue.dequeue()


def front(queue):
    return queue.front()


def priority_enqueue(queue, notification):
    queue.priority_enqueue(notification)


class FeedProcessor:
    def __init__(self):
        self.recent_activities = ActivityStack()
        self.notification_queue = NotificationQueue()
        self.processed_log = NotificationQueue()

    def process_incoming(self):
        notification = dequeue(self.notification_queue)
        if notification != "Queue Empty":
            push(self.recent_activities, notification)

    def batch_process(self, k):
        for _ in range(k):
            self.process_incoming()

    def clear_history(self):
        while is_empty(self.recent_activities) is False:
            activity = pop(self.recent_activities)
            enqueue(self.processed_log, activity)

    def get_stats(self):
        return size(self.recent_activities), size(self.notification_queue), size(self.processed_log)


def process_incoming(system):
    system.process_incoming()


def batch_process(system, k):
    system.batch_process(k)


def clear_history(system):
    system.clear_history()


def get_stats(system):
    return system.get_stats()


if __name__ == "__main__":
    print("Part A: Recent Activity Stack")
    activity_stack = ActivityStack()
    undo_stack = ActivityStack()

    push(activity_stack, "Liked a post")
    push(activity_stack, "Commented on a photo")
    push(activity_stack, "Shared a reel")
    push(activity_stack, "Updated profile")

    print("Top activity:", peek(activity_stack))
    print("Current stack size:", size(activity_stack))
    print("Most recent 3 activities:")
    display_recent(activity_stack, 3)

    print("Undo last activity:", undo_last(activity_stack, undo_stack))
    print("Top after undo:", peek(activity_stack))
    print("Undo stack top:", peek(undo_stack))

    print("\nPart B: Notification Queue")
    queue = NotificationQueue()
    enqueue(queue, "Friend request from Alex")
    enqueue(queue, "Message from Sam")
    enqueue(queue, "New follower: Mia")
    priority_enqueue(queue, "Urgent: Account security alert")

    print("Front notification:", front(queue))
    print("Queue size:", size(queue))
    print("Dequeue 2 notifications:")
    print(dequeue(queue))
    print(dequeue(queue))
    print("Front after dequeue:", front(queue))

    print("\nPart C: Integrated Feed Processing")
    system = FeedProcessor()
    enqueue(system.notification_queue, "Tagged in a post")
    enqueue(system.notification_queue, "Mentioned in a comment")
    priority_enqueue(system.notification_queue, "System maintenance notice")

    print("Stats before processing:", get_stats(system))
    batch_process(system, 2)
    print("Stats after batch_process(2):", get_stats(system))

    print("Recent activities:")
    display_recent(system.recent_activities, 5)

    clear_history(system)
    print("Stats after clear_history:", get_stats(system))

    print("Processed log entries:")
    while not is_empty(system.processed_log):
        print(dequeue(system.processed_log))
