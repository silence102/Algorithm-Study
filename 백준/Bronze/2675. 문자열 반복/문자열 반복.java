import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int S = scanner.nextInt();
        scanner.nextLine();
        
        for (int i = 0; i < S; i++) {
            int R = scanner.nextInt();
            String word = scanner.nextLine();
            String[] words = word.split("");

            for (int j = 0; j < words.length; j++) {
                words[j] = words[j].replaceAll(" ","");
                System.out.print(words[j].repeat(R));
            }
            System.out.println();
        }
    }
}
