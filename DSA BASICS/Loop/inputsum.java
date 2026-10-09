package Loop;
import java.util.Scanner;

public class inputsum {
    static void main() {
        Scanner sc= new Scanner(System.in);
        System.out.print("Enter your Size: ");
        int n= sc.nextInt();
        int arr[]= new int [n];
        int sum=0;
        for(int i=0;i<arr.length;i++){
            System.out.print("Enter your elements: ");
            arr[i]=sc.nextInt();
            sum= sum + arr[i];

        }
        System.out.print("Sum of array is : " + sum);

    }

}
