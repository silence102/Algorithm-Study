import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int M = scanner.nextInt();
        int[] numbers = new int[N];

        for (int i = 0; i < N; i++) 
            numbers[i] = i + 1;

        for (int cnt = 0; cnt < M; cnt++) {
            int i = scanner.nextInt();
            int j = scanner.nextInt(); 
            int num = 0;
            if (i == j) {
                continue;
            } else {
                if (((j - i) % 2) > 0) {
                    num = (j - i) / 2 + 1;
                } else {
                    num = (j - i) / 2;
                }
                for (int k = 0; k < num; k++, i++, j--) {
                    int changeNum = 0;
                    changeNum = numbers[i - 1];
                    numbers[i - 1] = numbers[j - 1];
                    numbers[j - 1] = changeNum;
                }
            }
        }
        for (int a = 0; a < N; a++) {
            System.out.print(numbers[a] + " ");
        }
    }
}