import java.util.Scanner;

public class Main {
    
    public static void main (String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            int X = scanner.nextInt();
            int Y = scanner.nextInt();
            
            if (X == 0 && Y == 0) {
                break;
            }
            int sum = X + Y;
            
            System.out.println(sum);
        }
    }
}