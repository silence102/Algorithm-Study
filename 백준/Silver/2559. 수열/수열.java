import java.util.Scanner;

public class Main {
    
    public static void main (String args[]) {       
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int K = scanner.nextInt();
        int numList[] = new int[N];
        for (int i = 0; i < N; i++) {
            numList[i] = scanner.nextInt();
        }
        
        int max_num = -10000000;
        int help = 0;
        int rule = K;
        
        for (int i = 0; i < numList.length - rule + 1; i++) {
            int sum_num = 0;
            for (int order = 0 + help; order < K; order++) {
                sum_num += numList[order];
            }
            help++;
            K++;
            if (sum_num > max_num) {
                max_num = sum_num;
            }
        }
        
        System.out.println(max_num);
    }
}