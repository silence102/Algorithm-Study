import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        String name = scanner.nextLine();
        
        if (name != null){
            System.out.println(name + "??!");
        }
    }
}