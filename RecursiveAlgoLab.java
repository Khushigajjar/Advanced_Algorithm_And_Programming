import java.util.*;

public class RecursiveAlgoLab {

    static class Comment {
        String text;
        List<Comment> replies = new ArrayList<>();

        public Comment(String text) {
            this.text = text;
        }

        public void addReply(Comment c) {
            replies.add(c);
        }

        public String toString() {
            return text;
        }
    }

    static final int STATE_START = 0;
    static final int STATE_DONE = 1;

    static class Frame {
        Comment c;
        int state;

        Frame(Comment c, int state) {
            this.c = c;
            this.state = state;
        }
    }

    // recursive flatten
    public static List<Comment> flattenRecursive(Comment c) {
        List<Comment> res = new ArrayList<>();
        res.add(c);

        for (Comment r : c.replies) {
            res.addAll(flattenRecursive(r));
        }
        return res;
    }

    // iterative flatten
    public static List<Comment> flattenIterative(Comment root) {
        List<Comment> res = new ArrayList<>();
        Stack<Frame> stack = new Stack<>();

        stack.push(new Frame(root, STATE_START));

        while (!stack.isEmpty()) {
            Frame f = stack.pop();

            if (f.state == STATE_START) {
                res.add(f.c);

                stack.push(new Frame(f.c, STATE_DONE));

                for (int i = f.c.replies.size() - 1; i >= 0; i--) {
                    stack.push(new Frame(f.c.replies.get(i), STATE_START));
                }
            }
        }
        return res;
    }

    // tail recursion count
    public static int countTail(Comment c, int acc) {
        acc++;

        for (Comment r : c.replies) {
            acc = countTail(r, acc);
        }
        return acc;
    }

    // loop count
    public static int countLoop(Comment root) {
        Stack<Comment> stack = new Stack<>();
        int count = 0;

        stack.push(root);

        while (!stack.isEmpty()) {
            Comment cur = stack.pop();
            count++;

            for (Comment r : cur.replies) {
                stack.push(r);
            }
        }
        return count;
    }

    public static void main(String[] args) {
        Comment root = new Comment("A");
        Comment b = new Comment("B");
        Comment c = new Comment("C");
        Comment d = new Comment("D");

        root.addReply(b);
        root.addReply(c);
        b.addReply(d);

        System.out.println(flattenRecursive(root));
        System.out.println(flattenIterative(root));
        System.out.println(countTail(root, 0));
        System.out.println(countLoop(root));
    }
}