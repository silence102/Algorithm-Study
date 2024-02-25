import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);    
        int N = scanner.nextInt();
        int[] subject = new int[N];
        int max = 0;
        double sum = 0;
        
        for (int i = 0; i < N; i++) {
            int score = scanner.nextInt();
            subject[i] = score;
            if (max == 0) {
                max = subject[i];
            } else {
                if (subject[i] > max) {
                    max = subject[i];
                }
            }   
        }
        for (int i = 0; i < N; i++) {
            double divide = (double) subject[i] / max;
            sum += (divide * 100);
        }
        double result = sum / N;
        System.out.println(result);
    }
}