// Example 1 (Java)

public class BubbleSort {
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // swap arr[j] and arr[j+1]
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        bubbleSort(arr);
        System.out.println("Sorted array is:");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}

/**
 * The BubbleSort class provides a static method to perform bubble sort on an array of integers.
 * It also includes a main method to demonstrate the sorting algorithm.
 */
public class BubbleSort {

    /**
     * Sorts the specified array of integers using the bubble sort algorithm.
     *
     * <p>The bubble sort algorithm repeatedly steps through the list, compares adjacent elements
     * and swaps them if they are in the wrong order. The pass through the list is repeated until
     * the list is sorted. The algorithm is known for its simplicity but is inefficient for large lists.</p>
     *
     * @param arr the array of integers to be sorted
     */
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // swap arr[j] and arr[j+1]
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    /**
     * The main method serves as an entry point for the application. It demonstrates
     * the usage of the bubbleSort method by sorting a sample array of integers and
     * printing the sorted array to the standard output.
     *
     * @param args command-line arguments (not used)
     */
    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        bubbleSort(arr);
        System.out.println("Sorted array is:");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}
