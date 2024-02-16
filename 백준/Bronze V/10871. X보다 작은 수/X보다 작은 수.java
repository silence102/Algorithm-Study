import java.util.Scanner;

public class Main {
    
    public static void main (String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int X = scanner.nextInt();        
        int[] numList = new int[N];
        
        for (int i = 0; i < N; i++) {
            int A = scanner.nextInt();
            numList[i] = A;
            if (numList[i] < X) {
                System.out.print(numList[i] + " ");
            }
        }
    }
}