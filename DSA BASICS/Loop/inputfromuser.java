import java.util.Scanner;

public class inputfromuser {
    public static void main(String[]args){
       Scanner sc=new Scanner (System.in);
       System.out.print("Enter your number:");
       int arr[]=new int[5];
       for(int i=0;i<5;i++){
     arr[i]=sc.nextInt();
     
       }
       for(int i=0;i<arr.length-1;i++){
        System.out.print(arr[i]+" ");

       }
    }
    
}
