import java.util.Scanner;

public class Main {
    
    public static void main (String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int N = scanner.nextInt();
        int[] numList = new int[N];
        int minNumber = numList[0];
        int maxNumber = numList[0];
        
        for (int i = 0; i < N; i++) {
            numList[i] = scanner.nextInt();
            if (minNumber == 0 && maxNumber == 0) {
                minNumber = numList[0];
                maxNumber = numList[0];
            }
            if (minNumber > numList[i])
                minNumber = numList[i];
            if (maxNumber < numList[i])
                maxNumber = numList[i];   
        }
        System.out.print(minNumber + " ");
        System.out.print(maxNumber); 
    }
}