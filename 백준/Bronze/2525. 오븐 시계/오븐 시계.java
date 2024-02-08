import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int A = scanner.nextInt();
        int B = scanner.nextInt();
        int C = scanner.nextInt();
        
        int cook = A * 60 + B + C;
        int time = 24 * 60;
        
        if (cook < time) {
            System.out.println(cook / 60);
            System.out.println(cook % 60);            
        } else if (cook >= time) {
            System.out.println((cook - time) / 60);
            System.out.println((cook - time) % 60);
        }
        
    }
}