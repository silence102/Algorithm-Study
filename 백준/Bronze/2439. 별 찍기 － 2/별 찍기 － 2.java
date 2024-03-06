import java.util.Scanner;

public class Main {
    
    public static void main (String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        String[] stars = new String[N];

        for (int i = N-1; i >= 0; i--) {
            stars[i] = "*";

            for (int j = 0; j < N; j++) {
                if (stars[j] == null) {
                    stars[j] = " ";
                }
                System.out.print(stars[j]);
            }
            System.out.println();
        }
    }
}