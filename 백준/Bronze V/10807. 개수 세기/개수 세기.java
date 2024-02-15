import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int N = scanner.nextInt();      
        int[] numList = new int[N];
        int cnt = 0;
        
        for (int i = 0; i < N; i++) {
            int n = scanner.nextInt();
            numList[i] = n;
        }
        
        int v = scanner.nextInt();
        
        for (int i = 0; i < N; i++) {
            if (numList[i] == v) {
                cnt += 1;
            }
        }
        System.out.println(cnt);   
    }
}