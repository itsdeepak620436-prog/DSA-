package Loop;
import java.util.Scanner;
public class productarrays {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter your size of array: ");
        int n=sc.nextInt();
        int arr[]= new int[n];
        int product=1;
        for(int i=0;i<arr.length;i++){
            System.out.print("Enter your Elements: ");
            arr[i]=sc.nextInt();
            product=product*arr[i];
        }
        System.out.print("Your product is : " + product);

    }
}
