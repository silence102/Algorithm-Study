import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] numbers = new int[42];
        int cnt = 0;
        
        for (int i = 0; i < 10; i++) {
            int num = scanner.nextInt();
            int remainder = num % 42;
            
            for (int j = 0; j < 42; j++) {
                if (remainder == j) {
                    numbers[j] += 1;                    
                }
            }
        }
        for (int i = 0; i < 42; i++) {
            if (numbers[i] != 0) {
                cnt += 1;
            }  
        }
        System.out.println(cnt);
    }
}