import java.util.Scanner;

public class Main {
    
    public static void main (String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt(); 
        int M = scanner.nextInt();
        int[] numList = new int[N];
        
        for (int i = 0; i < N; i++) {
            numList[i] = i + 1;
        }
        for (int i = 0; i < M; i++) {
            int X = scanner.nextInt(); 
            int Y = scanner.nextInt();
            int num = 0;
            num = numList[X-1];
            numList[X-1] = numList[Y-1];
            numList[Y-1] = num;
        }
        for (int i = 0; i < N; i++) {
            int printNum = numList[i];
            System.out.print(printNum + " ");
        }
    }
}