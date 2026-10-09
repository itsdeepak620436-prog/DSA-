public class Insertion {
    public static void main(String[] args) {
        int[]arr={10,20,30,40,50};
        int indexposn=2;
        int element=25;
        int[]newarr=new int[arr.length+1];
        for(int i=0;i<indexposn;i++){
            newarr[i]=arr[i];
            System.out.print(arr[i]+" ");
        }
        newarr[indexposn]=element;
        System.out.print(element+" ");
        for(int i=indexposn;i<arr.length;i++){
            newarr[i]=arr[i];
            System.out.print(arr[i]+" ");
        }
    }
}