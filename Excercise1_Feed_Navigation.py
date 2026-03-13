class StoryNode:
    def __init__(self, story_id, content):
        self.story_id = story_id
        self.content = content
        self.views = 0
        self.next = None
        self.prev = None

class StoryFeed:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.size = 0

    def add_story(self, node):
            if self.head is None:
                self.head = node
                self.tail = node
                self.current = node
                
            else:
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
                
            self.size = self.size + 1

    def remove_story(self, story_id):
            target = self.head
            while target and target.story_id != story_id:
                target = target.next
                
            if target is None:
                return
            
            if target.prev:
                target.prev.next = target.next
            else:
                self.head = target.next

            if target.next:
                target.next.prev = target.prev
            else:
                self.tail = target.prev

            if self.current == target:
                self.current = target.next if target.next else target.prev

            self.size = self.size - 1

    def move_forward(self):
            if self.current is None or self.current.next is None:
                return None

            self.current = self.current.next
            return self.current
        
    def move_backward(self):
            if self.current is None or self.current.prev is None:
                return None

            self.current = self.current.prev
            return self.current
        
    def jump_to(self, story_id):
            node = self.head

            while node:
                if node.story_id == story_id:
                    self.current = node
                    return True
                node = node.next

            return False
        
    def insert_after(self, current_id, new_story):
            target = self.head

            while target and target.story_id != current_id:
                target = target.next

            if target is None:
                return

            new_story.prev = target
            new_story.next = target.next

            if target.next:
                target.next.prev = new_story
            else:
                self.tail = new_story

            target.next = new_story
            self.size = self.size + 1

    def display_around_current(self, k):

            node = self.current
            i = 0

            while node.prev and i < k:
                node = node.prev
                i += 1

            count = 0

            while node and count <= 2*k:
                print(node.content)
                node = node.next
                count = count + 1

    def track_view(self):
            if self.current:
                self.current.views = self.current.views + 1

        
    def most_viewed(self):
            best = self.head
            node = self.head

            while node:
                if node.views > best.views:
                    best = node
                node = node.next

            return best
        
    def reorder_by_views(self):
            nodes = []
            node = self.head

            while node:
                nodes.append(node)
                node = node.next

            n = len(nodes)

            for i in range(1, n):

                key = nodes[i]
                j = i - 1

                while j >= 0 and nodes[j].views < key.views:
                    nodes[j+1] = nodes[j]
                    j -= 1

                nodes[j+1] = key

            self.head = nodes[0]

            for i in range(n-1):
                nodes[i].next = nodes[i+1]
                nodes[i+1].prev = nodes[i]

            nodes[n-1].next = None
            self.tail = nodes[n-1]

    def display(self):

            node = self.head

            while node:
                print(f"[{node.story_id}: {node.content}] Views:{node.views}", end=" <-> ")
                node = node.next

            print("NULL")


feed = StoryFeed()

s1 = StoryNode(1,"Morning coffee")
s2 = StoryNode(2,"Workout complete")
s3 = StoryNode(3,"Sunset photo")

feed.add_story(s1)
feed.add_story(s2)
feed.add_story(s3)

print("Initial Feed:")
feed.display()


feed.jump_to(2)
feed.track_view()
feed.track_view()

feed.jump_to(3)
feed.track_view()

print("\nAfter viewing:")
feed.display()


feed.reorder_by_views()

print("\nAfter reorder_by_views():")
feed.display()













