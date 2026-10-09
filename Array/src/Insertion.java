public class Insertion {
    static void main() {
        int[] arr = {10, 20, 30, 40, 50, 60};
        int indexpos = 6;
        int element = 100;
        int[] newarr = new int[arr.length + 1];
        for (int i = 0; i < indexpos; i++) {
            newarr[i] = arr[i];
            System.out.print(arr[i]);
        }

        newarr[indexpos] = element;
        System.out.print(element);
 for(int i =indexpos;i<arr.length;i++){
     newarr[i+1]=arr[i];
     System.out.print(arr[i]+" ");
        }

    }

}
