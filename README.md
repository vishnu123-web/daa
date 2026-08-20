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

# practical_2
Summary
The binary_search() function repeatedly divides the search range into two halves. It compares the target value with the middle element and eliminates the half of the list where the target cannot exist. This process continues until the target is found or the search range becomes empty.
The program also uses time.perf_counter() to measure and display the execution time of the binary search operation. If the target is found, its index in the sorted list is displayed; otherwise, the program reports that the target was not found.
Time Complexity:
Best Case: O(1)
Average Case: O(log n)
Worst Case: O(log n)
Space Complexity: O(1)
Conclusion
Binary Search is an efficient searching algorithm, especially for large sorted datasets. By eliminating half of the remaining elements after each comparison, it significantly reduces the number of operations required compared with a linear search.
The program demonstrates that Binary Search has a worst-case time complexity of O(log n) and uses constant extra space, making it highly efficient. However, the list must be sorted before searching. Therefore, Binary Search is most beneficial when the data is already sorted or when the same sorted data will be searched multiple times.
# practical_3
 # Summary
In the Max-Heap Sort implementation, the elements are converted to negative values because Python's heapq provides a Min Heap by default. The elements are then repeatedly removed from the heap and converted back to positive values, producing the array in descending order. For example, [1, 5, 3] produces [5, 3, 1].
In the Min-Heap Sort implementation, the input list is directly converted into a Min Heap using heapq.heapify(). The smallest element is repeatedly removed from the heap, producing the array in ascending order. For example, [18, 7, 45] produces [7, 18, 45].
Both implementations have:
Best Case: O(n log n)
Average Case: O(n log n)
Worst Case: O(n log n)
The programs also calculate the actual execution time for the sorting operation.
# Conclusion
Heap Sort is an efficient sorting technique that provides a consistent O(n log n) time complexity in the best, average, and worst cases. The Min Heap can be used to sort elements in ascending order, while the Max Heap can be used to sort elements in descending order.
The programs demonstrate how heaps can be effectively used for sorting and how Python's heapq module simplifies heap operations. Compared with simpler sorting algorithms such as Bubble Sort and Selection Sort, Heap Sort is generally more suitable for larger datasets because its performance remains O(n log n) even in the worst case.

#practical_4
# summary
In the Iterative method, a for loop multiplies all integers from 1 to n to calculate the factorial. In the Recursive method, the function repeatedly calls itself with n-1 until it reaches the base case of 0 or 1.
For example, when the input is 5, both methods produce the result 120.
The time complexity of both methods is O(n) because they perform approximately n multiplication operations.
Iterative Time Complexity: O(n)
Recursive Time Complexity: O(n)
Iterative Space Complexity: O(1)
Recursive Space Complexity: O(n), due to the function call stack
The program also compares the execution times of the two approaches.
 # Conclusion
Both iterative and recursive methods successfully calculate the factorial of a number and have O(n) time complexity. The iterative approach generally uses less memory because it does not require recursive function calls, giving it an advantage for very large values of n.
The recursive approach is simpler and demonstrates the concept of recursion, but it requires additional stack memory and may encounter Python's recursion-depth limitation for sufficiently large inputs. Therefore, the iterative method is generally more memory-efficient, while the recursive method is useful for understanding and demonstrating recursive problem-solving.
