public class Deletion {
    static void main() {
        int[]arr={10,20,60,40,30};
        int indexposn=2;
        int[]newarr=new int[arr.length-1];
        int j=0;
        for(int i=0;i<arr.length;i++){
            if(i==indexposn){
                continue;
            }
            newarr[j]=arr[i];
            j++;
            System.out.print(arr[i]+" ");
        }


    }
}
