import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // Read N and K
        int N = scanner.nextInt();
        int K = scanner.nextInt();
        // Read the screenshots
        int[][] scores = new int[N][K];
        int[] indices = new int[N];
        for (int i = 0; i < N; i++) {
            indices[i] = i + 1; // Store the original indices
            for (int j = 0; j < K; j++) {
                scores[i][j] = scanner.nextInt();
            }
        }
        // Sort the screenshots lexicographically
        Integer[] order = new Integer[N];
        for (int i = 0; i < N; i++) {
            order[i] = i;
        }
        Arrays.sort(order, (a, b) -> {
            for (int j = 0; j < K; j++) {
                if (scores[a][j] != scores[b][j]) {
                    return Integer.compare(scores[a][j], scores[b][j]);
                }
            }
            return 0;
        });
        // Validate the sorted order
        for (int j = 0; j < K; j++) {
            for (int i = 1; i < N; i++) {
                if (scores[order[i]][j] < scores[order[i - 1]][j]) {
                    System.out.println("NO");
                    return;
                }
            }
        }
        // If valid, print "YES" and the order of indices
        System.out.println("YES");
        for (int i = 0; i < N; i++) {
            System.out.print(indices[order[i]] + " ");
        }
        System.out.println();
    }
}