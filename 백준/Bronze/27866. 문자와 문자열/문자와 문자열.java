import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String word = scanner.nextLine();
        int num = scanner.nextInt();
        
        System.out.println(word.substring(num-1,num));
    }
}