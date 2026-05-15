import java.util.*;

public class Main {

    static class Result {
        int influence;
        List<Integer> users;

        Result(int influence, List<Integer> users) {
            this.influence = influence;
            this.users = users;
        }
    }

    static Result maximizeReach(int budget, int[] costs, int[] influences) {
        int n = costs.length;
        int[][] dp = new int[n + 1][budget + 1];

        for (int i = 1; i <= n; i++) {
            for (int b = 0; b <= budget; b++) {
                dp[i][b] = dp[i - 1][b];

                if (costs[i - 1] <= b) {
                    int take = influences[i - 1] + dp[i - 1][b - costs[i - 1]];
                    if (take > dp[i][b]) {
                        dp[i][b] = take;
                    }
                }
            }
        }

        List<Integer> selected = new ArrayList<>();
        int b = budget;

        for (int i = n; i >= 1; i--) {
            if (dp[i][b] != dp[i - 1][b]) {
                selected.add(i - 1);
                b -= costs[i - 1];
            }
        }

        Collections.reverse(selected);
        return new Result(dp[n][budget], selected);
    }

    static boolean isWithinBudget(List<Integer> selection, int[] costs, int budget) {
        int total = 0;

        for (int i : selection) {
            total += costs[i];
        }

        return total <= budget;
    }

    static Result fastAlternative(int budget, int[] costs, int[] influences) {
        int n = costs.length;
        Integer[] ids = new Integer[n];

        for (int i = 0; i < n; i++) {
            ids[i] = i;
        }

        Arrays.sort(ids, (a, b) -> {
            double r1 = (double) influences[a] / costs[a];
            double r2 = (double) influences[b] / costs[b];
            return Double.compare(r2, r1);
        });

        int totalCost = 0;
        int totalInfluence = 0;
        List<Integer> selected = new ArrayList<>();

        for (int i : ids) {
            if (totalCost + costs[i] <= budget) {
                selected.add(i);
                totalCost += costs[i];
                totalInfluence += influences[i];
            }
        }

        return new Result(totalInfluence, selected);
    }

    public static void main(String[] args) {
        int budget = 10;

        int[] costs = {6, 5, 5, 3};
        int[] influences = {60, 49, 49, 20};

        Result exact = maximizeReach(budget, costs, influences);

        System.out.println("Exact influence: " + exact.influence);
        System.out.println("Selected users: " + exact.users);
        System.out.println("Within budget: " + isWithinBudget(exact.users, costs, budget));

        Result greedy = fastAlternative(budget, costs, influences);

        System.out.println("Greedy influence: " + greedy.influence);
        System.out.println("Selected users: " + greedy.users);
        System.out.println("Within budget: " + isWithinBudget(greedy.users, costs, budget));
    }
}