// example 2 (Javascript)

function bubbleSort(arr) {
    let n = arr.length;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                let temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}
let arr = [64, 34, 25, 12, 22, 11, 90];
console.log("Unsorted array:", arr);
bubbleSort(arr);
console.log("Sorted array is:", arr);


/**
 * Sorts an array of integers using the bubble sort algorithm.
 *
 * The bubble sort algorithm repeatedly steps through the list,
 * compares adjacent elements and swaps them if they are in the wrong order.
 * The pass through the list is repeated until the list is sorted.
 * The algorithm is known for its simplicity but is inefficient for large lists.
 *
 * @param {number[]} arr - The array of integers to be sorted.
 */
function bubbleSort(arr) {
    let n = arr.length;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Swap arr[j] and arr[j+1]
                let temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// Example usage
let arr = [64, 34, 25, 12, 22, 11, 90];
console.log("Unsorted array:", arr);
bubbleSort(arr);
console.log("Sorted array is:", arr);
