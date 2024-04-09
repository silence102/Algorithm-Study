import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String A = scanner.next();
        String B = scanner.next();
        String[] A1 = A.split("");
        String[] B1 = B.split("");
        String A2 = "";
        String B2 = "";
        
        for (int i = 2; i >= 0; i--) {
            A2 += A1[i];
            B2 += B1[i];
        }
        int A3 = Integer.parseInt(A2);
        int B3 = Integer.parseInt(B2);
        if (A3 > B3) {
            System.out.println(A2);
        } else {
            System.out.println(B2);
        }
    }
}