import java.util.Scanner;

public class Main {
    
    public static void main (String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int T = scanner.nextInt();
        
        for (int i = 1; i <= T; i++) {
            int X = scanner.nextInt();
            int Y = scanner.nextInt();
            int sum = X + Y;
            System.out.println("Case #" + i + ": " + sum);
        }
    }
}