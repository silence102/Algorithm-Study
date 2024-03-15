import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        scanner.nextLine();
        
        for (int i = 0; i < T; i++) {
            String word = scanner.nextLine();
            String[] list = word.split("");
            String answer = "";

            if (list.length != 1) {
                answer += list[0];
                answer += list[list.length-1];
            } else {
                answer += list[0];
                answer += list[0];
            }
            System.out.println(answer);
        }
    }
}