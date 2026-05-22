import java.util.*;

public class Main {

    static int countCrossEdges(List<Integer> a, List<Integer> b, List<List<Integer>> graph) {
        Set<Integer> setB = new HashSet<>(b);
        int count = 0;

        for (int u : a) {
            for (int v : graph.get(u)) {
                if (setB.contains(v)) {
                    count++;
                }
            }
        }
        return count;
    }

    static boolean balanced(List<Integer> a, List<Integer> b, int n) {
        int min = (int) Math.ceil(0.4 * n);
        return a.size() >= min && b.size() >= min;
    }

    static Result greedyPartition(List<List<Integer>> graph) {
        int n = graph.size();
        int min = (int) Math.ceil(0.4 * n);

        List<Integer> a = new ArrayList<>();
        List<Integer> b = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            if (i < n / 2) a.add(i);
            else b.add(i);
        }

        int best = countCrossEdges(a, b, graph);
        boolean changed = true;

        while (changed) {
            changed = false;

            for (int u = 0; u < n; u++) {
                List<Integer> from = a.contains(u) ? a : b;
                List<Integer> to = a.contains(u) ? b : a;

                if (from.size() - 1 < min) continue;

                from.remove(Integer.valueOf(u));
                to.add(u);

                int now = countCrossEdges(a, b, graph);

                if (now < best) {
                    best = now;
                    changed = true;
                } else {
                    to.remove(Integer.valueOf(u));
                    from.add(u);
                }
            }
        }

        return new Result(best, a, b);
    }

    static Result localSearch(List<List<Integer>> graph, int iterations) {
        Result best = null;

        for (int i = 0; i < iterations; i++) {
            Result current = greedyPartition(graph);

            if (best == null || current.crossEdges < best.crossEdges) {
                best = current;
            }
        }

        return best;
    }

    static class Result {
        int crossEdges;
        List<Integer> groupA;
        List<Integer> groupB;

        Result(int crossEdges, List<Integer> groupA, List<Integer> groupB) {
            this.crossEdges = crossEdges;
            this.groupA = new ArrayList<>(groupA);
            this.groupB = new ArrayList<>(groupB);
        }
    }

    public static void main(String[] args) {
        int n = 6;
        List<List<Integer>> graph = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }

        addEdge(graph, 0, 1);
        addEdge(graph, 0, 2);
        addEdge(graph, 1, 2);
        addEdge(graph, 3, 4);
        addEdge(graph, 4, 5);
        addEdge(graph, 3, 5);
        addEdge(graph, 2, 3);

        Result result = localSearch(graph, 5);

        System.out.println("Cross edges: " + result.crossEdges);
        System.out.println("Group A: " + result.groupA);
        System.out.println("Group B: " + result.groupB);
        System.out.println("Balanced: " + balanced(result.groupA, result.groupB, n));
    }

    static void addEdge(List<List<Integer>> graph, int u, int v) {
        graph.get(u).add(v);
        graph.get(v).add(u);
    }
}