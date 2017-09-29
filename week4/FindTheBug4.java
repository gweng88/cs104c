import java.util.*;

/*
 * The problem statement can be found at http://www.spoj.com/problems/AGGRCOW/
 * 
 * The online judge gives wrong answer, but the sample test case works. Can you
 * find the bug?
 */
public class FindTheBug4 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int t = 0; t < T; t++) {
            int numStalls = scanner.nextInt();
            int numCows = scanner.nextInt();
            List<Integer> stallPositions = new ArrayList<Integer>();
            for (int i = 0; i < numStalls; i++) {
                int pos = scanner.nextInt();
                stallPositions.add(pos);
            }
            Collections.sort(stallPositions);
            System.out.println(solve(stallPositions, numCows));
        }
    }

    private static int solve(List<Integer> stallPositions, int numCows) {
        int low = 0;
        int high = stallPositions.get(stallPositions.size() - 1);
        while (low < high) {
            int mid = (low + high) / 2;
            if (works(stallPositions, numCows, mid)) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return low;
    }

    private static boolean works(List<Integer> stallPositions, int numCows, int minDist) {
        int lastCowPosition = -minDist;
        for (int stallPosition : stallPositions) {
            if (stallPosition - lastCowPosition >= minDist) {
                lastCowPosition = stallPosition;
                numCows = Math.max(0, numCows - 1);
            }
        }

        return numCows == 0;
    }

}
