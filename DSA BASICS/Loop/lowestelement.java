package Loop;
public class lowestelement {
    static void main() {
        int[]arr={15,5,7,9,14,10};
        int min=arr[0];
        for(int i=0;i<arr.length;i++){
            if(arr[i]<min) min=arr[i];
        }
        System.out.print(min);
    }
}
