import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        scanner.nextLine();
        String num = scanner.nextLine();
        String[] numbers = new String[N];
        numbers = num.split("");
        int answer = 0;

        for (int i = 0; i < N; i++) {
            answer += Integer.parseInt(numbers[i]);
        }
        System.out.println(answer);
    }
}