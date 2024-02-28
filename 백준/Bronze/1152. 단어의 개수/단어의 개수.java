import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);        
        String sentence = scanner.nextLine();
        String[] word = sentence.split(" ");
        int cnt = 0;
        
        for (int i = 0; i < word.length; i++) {
            if (word[i].isEmpty()) {
                continue;
            }
            cnt += 1;
        }
        System.out.println(cnt);
    }
}