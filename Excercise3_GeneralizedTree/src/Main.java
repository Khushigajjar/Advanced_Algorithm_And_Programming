import java.util.*;

class GeneralizedCategoryNode {
    int id;
    String name;
    int postCount;
    List<GeneralizedCategoryNode> children;
    GeneralizedCategoryNode parent;

    public GeneralizedCategoryNode(int id, String name, int postCount) {
        this.id = id;
        this.name = name;
        this.postCount = postCount;
        this.children = new ArrayList<>();
    }
}

class BinaryTreeNode {
    int id;
    String name;
    int postCount;
    BinaryTreeNode left;
    BinaryTreeNode right;

    public BinaryTreeNode(int id, String name, int postCount) {
        this.id = id;
        this.name = name;
        this.postCount = postCount;
    }
}

class GeneralizedTree {

    public static GeneralizedCategoryNode binaryToGeneralized(BinaryTreeNode root) {
        if (root == null) return null;

        GeneralizedCategoryNode node =
                new GeneralizedCategoryNode(root.id, root.name, root.postCount);

        BinaryTreeNode cur = root.left;

        while (cur != null) {
            GeneralizedCategoryNode child = binaryToGeneralized(cur);
            child.parent = node;
            node.children.add(child);
            cur = cur.right;
        }

        return node;
    }

    public static BinaryTreeNode generalizedToBinary(GeneralizedCategoryNode root) {
        if (root == null) return null;

        BinaryTreeNode node =
                new BinaryTreeNode(root.id, root.name, root.postCount);

        if (root.children.size() == 0) return node;

        node.left = generalizedToBinary(root.children.get(0));
        BinaryTreeNode cur = node.left;

        for (int i = 1; i < root.children.size(); i++) {
            cur.right = generalizedToBinary(root.children.get(i));
            cur = cur.right;
        }

        return node;
    }

    public static void preOrder(GeneralizedCategoryNode node) {
        if (node == null) return;

        System.out.print(node.name + " ");
        for (GeneralizedCategoryNode c : node.children) {
            preOrder(c);
        }
    }

    public static void postOrder(GeneralizedCategoryNode node) {
        if (node == null) return;

        for (GeneralizedCategoryNode c : node.children) {
            postOrder(c);
        }
        System.out.print(node.name + " ");
    }

    public static void levelOrder(GeneralizedCategoryNode root) {
        if (root == null) return;

        Queue<GeneralizedCategoryNode> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {
            GeneralizedCategoryNode cur = q.poll();
            System.out.print(cur.name + " ");

            for (GeneralizedCategoryNode c : cur.children) {
                q.add(c);
            }
        }
    }

    public static int countNodes(GeneralizedCategoryNode node) {
        if (node == null) return 0;

        int res = 1;
        for (GeneralizedCategoryNode c : node.children) {
            res += countNodes(c);
        }
        return res;
    }

    public static int countLeaves(GeneralizedCategoryNode node) {
        if (node == null) return 0;

        if (node.children.size() == 0) return 1;

        int res = 0;
        for (GeneralizedCategoryNode c : node.children) {
            res += countLeaves(c);
        }
        return res;
    }

    public static int height(GeneralizedCategoryNode node) {
        if (node == null) return -1;

        if (node.children.size() == 0) return 0;

        int max = 0;
        for (GeneralizedCategoryNode c : node.children) {
            int h = height(c);
            if (h > max) max = h;
        }
        return max + 1;
    }

    public static int fanOut(GeneralizedCategoryNode node) {
        if (node == null) return 0;

        int max = node.children.size();
        for (GeneralizedCategoryNode c : node.children) {
            int f = fanOut(c);
            if (f > max) max = f;
        }
        return max;
    }

    public static double branchingFactor(GeneralizedCategoryNode root) {
        int[] r = calc(root);
        if (r[1] == 0) return 0;
        return (double) r[0] / r[1];
    }

    private static int[] calc(GeneralizedCategoryNode node) {
        if (node == null) return new int[]{0, 0};

        int sum = 0;
        int count = 0;

        if (node.children.size() > 0) {
            sum += node.children.size();
            count++;
        }

        for (GeneralizedCategoryNode c : node.children) {
            int[] t = calc(c);
            sum += t[0];
            count += t[1];
        }

        return new int[]{sum, count};
    }

    public static void main(String[] args) {

        GeneralizedCategoryNode root = new GeneralizedCategoryNode(1, "Tech", 0);
        GeneralizedCategoryNode a = new GeneralizedCategoryNode(2, "Prog", 0);
        GeneralizedCategoryNode b = new GeneralizedCategoryNode(3, "Design", 0);

        root.children.add(a);
        root.children.add(b);

        a.children.add(new GeneralizedCategoryNode(4, "Java", 0));
        a.children.add(new GeneralizedCategoryNode(5, "Python", 0));

        System.out.print("Pre: ");
        preOrder(root);
        System.out.println();

        System.out.print("Level: ");
        levelOrder(root);
        System.out.println();

        System.out.println("Nodes: " + countNodes(root));
        System.out.println("Leaves: " + countLeaves(root));
        System.out.println("Height: " + height(root));
        System.out.println("FanOut: " + fanOut(root));
        System.out.println("BF: " + branchingFactor(root));
    }
}