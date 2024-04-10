import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] chess = {"1", "1", "2", "2", "2", "8"};
        for (int i = 0; i < 6; i++) {
            String play = scanner.next();
            String comp = chess[i];
            int playI = Integer.parseInt(play);
            int compI = Integer.parseInt(comp);
            int num = 0;
            if (playI > compI) {
                for (int j = playI-1; j >= compI; j--) {
                    num -= 1;
                    if (j == compI) {
                        System.out.print(num + " ");
                    }
                }
            } else if (playI < compI) {
                for (int j = playI+1; j <= compI; j++) {
                    num += 1;
                    if (j == compI) {
                        System.out.print(num + " ");
                    }
                }
            } else {
                System.out.print("0 ");
            }
        }
    }
}