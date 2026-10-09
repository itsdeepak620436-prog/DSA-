public class Searching {
    static void main() {
        int[] arr = {10, 20, 30, 40, 50};
        int element = 50;
        boolean found = false;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == element) {
                System.out.print("Element found at index :" + i);
                found = true;
                break;
            }

            }
        if (found == false) {
            System.out.print("Element not found");
        }
    }
}


