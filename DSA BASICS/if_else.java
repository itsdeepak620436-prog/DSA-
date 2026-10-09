import java.util.Scanner;
public class if_else {
    public static void main(String[] args) {
        System.out.print("Enter your number:");
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        if(n%2==0){
            System.out.print("Number is Even");
        }else{
            System.out.print("Number is not even or number is odd");
        }
    }
}
