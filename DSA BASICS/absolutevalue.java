
import java.util.Scanner;
public class absolutevalue {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
         System.out.print("Enter your number:");
         int n=sc.nextInt();
         if(n>=0)
            System.out.print(n);
        else
            System.out.print(-n);
    }
    
}
