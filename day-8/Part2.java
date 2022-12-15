import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Part2 {
    public static void main(String[] args) throws IOException {
        final int width = 99;
        final int height = 99;
        final int[][] trees = new int[height][width];
        // up, right, down, left (y, x)
        final int[][] offsets = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

        final BufferedReader in = new BufferedReader(new FileReader("input"));

        for (int i = 0; i < height; i++) {
            final String line = in.readLine();
            trees[i] = line.chars().map(c -> c - '0').toArray();
        }
        in.close();

        int highestScore = -1;
        // for each tree... (we can skip the edges, they all have a score of 0)
        for (int y = 1; y < height - 1; y++) {
            for (int x = 1; x < width - 1; x++) {
                final int treeHeight = trees[y][x];
                int scenicScore = 1;
                // for each direction...
                for (int[] offset : offsets) {
                    int count = 0;
                    final int oy = offset[0];
                    final int ox = offset[1];
                    for (int i = 1; ; i++) {
                        final int ny = y + (oy * i);
                        final int nx = x + (ox * i);
                        // check bounds
                        if (ny < 0 || ny >= height || nx < 0 || nx >= width) {
                            break;
                        }
                        count++;
                        if (treeHeight <= trees[ny][nx]) {
                            break;
                        }
                    }

                    scenicScore *= count;
                }

                highestScore = Math.max(highestScore, scenicScore);
            }
        }

        System.out.println(highestScore);
    }
}
