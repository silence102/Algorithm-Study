import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] numList = new int[9];
        int maxNum = 0;
        int maxList = 0;
        
        for (int i = 0; i < 9; i++) {
            numList[i] = scanner.nextInt();
            if (numList[i] > maxNum) {
                maxNum = numList[i];
                maxList = i;
            }
        }
        System.out.println(maxNum);
        System.out.println(maxList + 1);
    }
}