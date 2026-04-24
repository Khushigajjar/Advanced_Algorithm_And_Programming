import java.util.*;

public class Main {

    // ===== Trie =====
    static class Node {
        Node[] next = new Node[26];
        boolean end;
        int id;
    }

    static Node root = new Node();

    static void insert(String s, int id) {
        Node cur = root;
        for (int i = 0; i < s.length(); i++) {
            int c = s.charAt(i) - 'a';
            if (cur.next[c] == null) cur.next[c] = new Node();
            cur = cur.next[c];
        }
        cur.end = true;
        cur.id = id;
    }

    static Integer search(String s) {
        Node cur = root;
        for (int i = 0; i < s.length(); i++) {
            int c = s.charAt(i) - 'a';
            if (cur.next[c] == null) return null;
            cur = cur.next[c];
        }
        if (cur.end) return cur.id;
        return null;
    }

    static boolean startsWith(String s) {
        Node cur = root;
        for (int i = 0; i < s.length(); i++) {
            int c = s.charAt(i) - 'a';
            if (cur.next[c] == null) return false;
            cur = cur.next[c];
        }
        return true;
    }

    static void collect(Node cur, String path, List<String> res, int k) {
        if (res.size() >= k) return;

        if (cur.end) res.add(path);

        for (int i = 0; i < 26; i++) {
            if (cur.next[i] != null) {
                collect(cur.next[i], path + (char)(i + 'a'), res, k);
            }
        }
    }

    static List<String> autocomplete(String s, int k) {
        List<String> res = new ArrayList<>();
        Node cur = root;

        for (int i = 0; i < s.length(); i++) {
            int c = s.charAt(i) - 'a';
            if (cur.next[c] == null) return res;
            cur = cur.next[c];
        }

        collect(cur, s, res, k);
        return res;
    }

    // ===== Segment Tree =====
    static int[] tree;
    static int n;

    static void build(int[] a, int i, int l, int r) {
        if (l == r) {
            tree[i] = a[l];
            return;
        }
        int m = (l + r) / 2;
        build(a, i * 2, l, m);
        build(a, i * 2 + 1, m + 1, r);
        tree[i] = tree[i * 2] + tree[i * 2 + 1];
    }

    static int query(int i, int l, int r, int ql, int qr) {
        if (qr < l || r < ql) return 0;
        if (ql <= l && r <= qr) return tree[i];
        int m = (l + r) / 2;
        return query(i * 2, l, m, ql, qr)
                + query(i * 2 + 1, m + 1, r, ql, qr);
    }

    // ===== main =====
    public static void main(String[] args) {

        // Trie test
        insert("alice", 1);
        insert("alex", 2);
        insert("bob", 3);

        System.out.println(search("alice"));      // 1
        System.out.println(startsWith("al"));     // true
        System.out.println(autocomplete("al", 5)); // [alex, alice] or similar

        // Segment tree test
        int[] a = {5, 3, 8, 6, 2};
        n = a.length;
        tree = new int[4 * n];

        build(a, 1, 0, n - 1);

        System.out.println(query(1, 0, n - 1, 1, 3)); // 17
    }
}