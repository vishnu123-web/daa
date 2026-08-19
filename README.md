# practical_1
Summary:-
In this experiment, five sorting algorithms were implemented and analyzed: Bubble Sort,
Selection Sort,
Insertion Sort, Merge Sort, and Quick Sort.
Each algorithm takes a list of numbers as input, sorts the elements in ascending order, and measures the execution time.
Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.
It is simple but inefficient for large datasets.
Selection Sort finds the smallest element from the unsorted portion and places it in the correct position.
Its performance remains O(n²) in all cases.
Insertion Sort inserts each element into its proper position within the sorted portion of the array.
It performs well for small or nearly sorted datasets.
Merge Sort follows the divide-and-conquer approach by splitting the array into smaller parts, sorting them, and then merging them.
It provides consistent O(n log n) performance.
Quick Sort selects a pivot element and partitions the array into smaller and larger elements before recursively sorting them.
It is generally one of the fastest sorting algorithms in practice.
The execution time and complexity analysis help compare the efficiency of these sorting techniques for different input sizes.

Conclusion:-
From the analysis, it is observed that Bubble Sort, Selection Sort,
and Insertion Sort are suitable for small datasets but become inefficient as the number of elements increases because of their O(n²) time complexity.
Merge Sort and Quick Sort perform much better for large datasets with an average time complexity of O(n log n).
Among all the algorithms, Quick Sort is generally the fastest in practical applications,
while Merge Sort provides stable and predictable performance. Therefore, for large amounts of data
Merge Sort and Quick Sort are preferred, whereas Insertion Sort can be useful for small or nearly sorted datasets.
The experiment demonstrates the importance of choosing the appropriate sorting algorithm based on the size and nature of the data.
