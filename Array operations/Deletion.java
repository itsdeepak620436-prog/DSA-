public class Deletion {
    public static void main(String[] args) {
        int[]arr={50,60,70,80,90,100};
        int indexposition=5;
        int[]newarr=new int[arr.length-1];
        int j=0;
        for(int i=0;i<arr.length;i++){
            if(i==indexposition){
                continue;
            }
            newarr[j]=arr[i];
            j++;
            System.out.print(arr[i]+" ");
        }
    }
    
}
