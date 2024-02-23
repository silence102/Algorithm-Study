import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] students = new int[30];
        int min = 0;
        int next = 0;
        
        for (int i = 0; i < 30; i++) {
            students[i] = i + 1;
        }
        for (int i = 0; i < 28; i++) {
            int attend = scanner.nextInt();
            for (int j = 0; j < 30; j++) {
                if (students[j] == attend) {
                    students[j] = 0;
                }
            }
        }
        for (int i = 0; i < 30; i++) {
            if (students[i] == 0) {
                continue;
            }
            else {
                if (min == 0) {
                    min = students[i];    
                }
                if (min > students[i]) {
                    next = min;
                    min = students[i];
                } else if (min < students[i]) {
                    next = students[i];
                }
            }
        }
        System.out.println(min);
        System.out.println(next);
    }
}