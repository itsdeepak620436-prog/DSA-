package Loop;
import java.util.Scanner;
public class numberofelements {
    static void main() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your size: ");
        int n = sc.nextInt();
        int arr[] = new int[n];
        for (int i = 0; i < arr.length; i++) {
            System.out.print("Enter your elements:");
            arr[i]=sc.nextInt();
        }
        System.out.print("maximum number of elements are : " + arr.length);
    }
}
