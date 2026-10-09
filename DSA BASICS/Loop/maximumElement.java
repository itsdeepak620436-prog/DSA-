package Loop;
public class maximumElement {
    static void main() {
        int[]arr={1,2,5,7,9,10,15,65};
        int max=arr[0];
        for(int i=0;i<arr.length;i++){
            if(arr[i]>max) max=arr[i];
        }
        System.out.print("Maximum is :" + max);
    }
}
