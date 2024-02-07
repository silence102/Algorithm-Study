import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int H = scanner.nextInt();
        int M = scanner.nextInt();
        int time = H * 60 + M - 45;
        if (time >= 0) {
            System.out.println(time / 60);
            System.out.println(time % 60);
        } else if ( time < 0) {
            System.out.println((24 * 60 + time) / 60);
            System.out.println((24 * 60 + time) % 60);
        }
    }
}