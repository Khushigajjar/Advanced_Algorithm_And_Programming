import java.util.ArrayList;
import java.util.List;

public class Main {

    // Post structure
    static class Post {
        int postId;
        int userId;
        String content;
        long timestamp; // store as milliseconds
        int likes;
        int comments;
        int shares;
        int engagementScore;

        public Post(int postId, int userId, String content, long timestamp,
                    int likes, int comments, int shares) {
            this.postId = postId;
            this.userId = userId;
            this.content = content;
            this.timestamp = timestamp;
            this.likes = likes;
            this.comments = comments;
            this.shares = shares;
            this.engagementScore = computeScore();
        }

        public int computeScore() {
            return likes * 1 + comments * 2 + shares * 3;
        }

        public void updateScore() {
            this.engagementScore = computeScore();
        }

        @Override
        public String toString() {
            return "[Post" + postId + ": score " + engagementScore + "]";
        }
    }

    // Node for singly linked list
    static class Node {
        Post post;
        Node next;

        public Node(Post post) {
            this.post = post;
            this.next = null;
        }
    }

    // Priority Queue using sorted singly linked list
    static class PriorityQueue {
        private Node head;
        private int size;

        public PriorityQueue() {
            this.head = null;
            this.size = 0;
        }

        // Check if queue is empty
        public boolean isEmpty() {
            return head == null;
        }

        // Return size
        public int size() {
            return size;
        }

        // Insert post while maintaining descending order of engagementScore
        public void enqueue(Post post) {
            post.updateScore();
            Node newNode = new Node(post);

            if (head == null || post.engagementScore > head.post.engagementScore) {
                newNode.next = head;
                head = newNode;
            } else {
                Node current = head;
                while (current.next != null &&
                        current.next.post.engagementScore >= post.engagementScore) {
                    current = current.next;
                }
                newNode.next = current.next;
                current.next = newNode;
            }
            size++;
        }

        // Remove and return highest priority post
        public Post dequeueMax() {
            if (head == null) {
                return null;
            }

            Post maxPost = head.post;
            head = head.next;
            size--;
            return maxPost;
        }

        // View highest priority post without removing
        public Post peekMax() {
            if (head == null) {
                return null;
            }
            return head.post;
        }

        // Update a specific post's likes/comments/shares and reinsert in sorted position
        public void updateScore(int postId, int newLikes, int newComments, int newShares) {
            if (head == null) {
                return;
            }

            Node current = head;
            Node prev = null;

            // Find the node
            while (current != null && current.post.postId != postId) {
                prev = current;
                current = current.next;
            }

            // Post not found
            if (current == null) {
                return;
            }

            // Remove node from current position
            if (prev == null) {
                head = current.next;
            } else {
                prev.next = current.next;
            }
            size--;

            // Update metrics
            current.post.likes = newLikes;
            current.post.comments = newComments;
            current.post.shares = newShares;
            current.post.updateScore();

            // Reinsert
            enqueue(current.post);
        }

        // Recalculate all scores and re-sort entire queue
        public void refreshAll() {
            List<Post> allPosts = new ArrayList<>();
            Node current = head;

            while (current != null) {
                current.post.updateScore();
                allPosts.add(current.post);
                current = current.next;
            }

            head = null;
            size = 0;

            for (Post post : allPosts) {
                enqueue(post);
            }
        }

        // Return top k highest priority posts
        public List<Post> getTopK(int k) {
            List<Post> result = new ArrayList<>();
            Node current = head;
            int count = 0;

            while (current != null && count < k) {
                result.add(current.post);
                current = current.next;
                count++;
            }

            return result;
        }

        // Reduce scores of posts older than given timestamp by 20%, then refresh order
        public void decayOlderThan(long cutoffTimestamp) {
            Node current = head;

            while (current != null) {
                if (current.post.timestamp < cutoffTimestamp) {
                    current.post.likes = (int) (current.post.likes * 0.8);
                    current.post.comments = (int) (current.post.comments * 0.8);
                    current.post.shares = (int) (current.post.shares * 0.8);
                    current.post.updateScore();
                }
                current = current.next;
            }

            refreshAll();
        }

        // Print queue
        public void printQueue() {
            Node current = head;
            while (current != null) {
                System.out.print(current.post);
                if (current.next != null) {
                    System.out.print(" -> ");
                }
                current = current.next;
            }
            System.out.println();
        }
    }

    // Main method for testing
    public static void main(String[] args) {
        PriorityQueue queue = new PriorityQueue();

        long now = System.currentTimeMillis();
        long oneHourAgo = now - 3600_000;

        Post post1 = new Post(1, 101, "Hello World", now, 10, 15, 14);   // score = 10 + 30 + 42 = 82
        Post post2 = new Post(2, 102, "Java is fun", now, 20, 9, 3);      // score = 20 + 18 + 9 = 47
        Post post3 = new Post(3, 103, "Trending post", oneHourAgo, 20, 18, 13); // score = 20 + 36 + 39 = 95
        Post post4 = new Post(4, 104, "Low priority", now, 5, 3, 4);      // score = 5 + 6 + 12 = 23

        queue.enqueue(post1);
        queue.enqueue(post2);
        queue.enqueue(post3);
        queue.enqueue(post4);

        System.out.println("Initial queue:");
        queue.printQueue();

        System.out.println("\nPeek max:");
        System.out.println(queue.peekMax());

        System.out.println("\nUpdate Post2 score:");
        queue.updateScore(2, 30, 9, 3); // new score = 30 + 18 + 9 = 57
        queue.printQueue();

        System.out.println("\nTop 3 posts:");
        List<Post> topPosts = queue.getTopK(3);
        for (Post p : topPosts) {
            System.out.println(p);
        }

        System.out.println("\nApply decay to posts older than now - 30 min:");
        long thirtyMinutesAgo = now - 1800_000;
        queue.decayOlderThan(thirtyMinutesAgo);
        queue.printQueue();

        System.out.println("\nDequeue max:");
        System.out.println(queue.dequeueMax());
        queue.printQueue();

        System.out.println("\nQueue size:");
        System.out.println(queue.size());
    }
}