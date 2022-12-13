import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Part1 {
    public static void main(String[] args) throws IOException {
        final int width = 99;
        final int height = 99;
        final int[][] trees = new int[height][width];
        final boolean[][] visibleMask = new boolean[height][width];
        final BufferedReader in = new BufferedReader(new FileReader("input"));

        for (int i = 0; i < height; i++) {
            final String line = in.readLine();
            trees[i] = line.chars().map(c -> c - '0').toArray();
        }
        in.close();

        // left to right
        for (int i = 0; i < height; i++) {
            int tallest = -1;
            for (int j = 0; j < width; j++) {
                if (trees[i][j] > tallest) {
                    visibleMask[i][j] = true;
                    tallest = Math.max(tallest, trees[i][j]);
                }
            }
        }

        // right to left
        for (int i = 0; i < height; i++) {
            int tallest = -1;
            for (int j = height - 1; j >= 0; j--) {
                if (trees[i][j] > tallest) {
                    visibleMask[i][j] = true;
                    tallest = Math.max(tallest, trees[i][j]);
                }
            }
        }

        // top to bottom
        for (int j = 0; j < width; j++) {
            int tallest = -1;
            for (int i = 0; i < height; i++) {
                if (trees[i][j] > tallest) {
                    visibleMask[i][j] = true;
                    tallest = Math.max(tallest, trees[i][j]);
                }
            }
        }

        // bottom to top
        for (int j = 0; j < width; j++) {
            int tallest = -1;
            for (int i = height - 1; i >= 0; i--) {
                if (trees[i][j] > tallest) {
                    visibleMask[i][j] = true;
                    tallest = Math.max(tallest, trees[i][j]);
                }
            }
        }

        // count visible
        int count = 0;
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                if (visibleMask[i][j]) {
                    count++;
                }
            }
        }

        System.out.println(count);
    }
}
