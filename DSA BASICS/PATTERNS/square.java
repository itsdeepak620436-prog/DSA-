import java.util.Scanner;

public class square {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter your first number:");
        int row=sc.nextInt();
        System.out.print("Enter your second number:");
        int col=sc.nextInt();
        for(int i=1;i<=row;i++){
            for(int j=1;j<=col;j++){
                System.out.print("* ");
            }
           System.out.println();
        }
    }
    
}
