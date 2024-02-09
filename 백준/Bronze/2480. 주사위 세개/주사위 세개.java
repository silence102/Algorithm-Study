import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int A  = scanner.nextInt();
        int B  = scanner.nextInt();
        int C  = scanner.nextInt();
        
        if (A == B & B == C) {
            System.out.println(10000 + A * 1000);
        } else if (A == B) {
            System.out.println(1000 + A * 100);
        } else if (B == C) {
            System.out.println(1000 + B * 100);
        } else if (C == A) {
            System.out.println(1000 + C * 100);
        } else {
            int max = 0;
            if (A > B) {
                max = A;
            } else {
                max = B;
            }
            if (max > C) {
                System.out.println(max * 100);
            } else {
                max = C;
                System.out.println(max * 100);
            }
        }
    }
}