# LeetCode Solutions Explanations

Here are the explanations for the solutions in this folder.

## 1.py - Two Sum
- **Code**: Uses a dictionary (`d`) to store numbers as keys and their indices as values. It iterates through `nums`, checks if `target - val` is in `d`, and returns the indices if found. Otherwise, it adds the current number and index to `d`.
- **Time Complexity**: O(n), where `n` is the number of elements in `nums`. Each element is visited at most once, and dictionary operations take O(1) on average.
- **Space Complexity**: O(n), as the dictionary can store up to `n` elements.

## 102.py - Binary Tree Level Order Traversal
- **Code**: Uses a queue-based Breadth-First Search (BFS) to traverse the tree level by level. It collects nodes at each level and stores them in a sub-list.
- **Time Complexity**: O(n), where `n` is the number of nodes in the tree. Every node is visited once.
- **Space Complexity**: O(n), as the queue and the result list can store up to `n` nodes.

## 1038.py - Binary Search Tree to Greater Sum Tree
- **Code**: Performs a DFS to collect all values into a list and maps them to nodes in a dictionary. It then sorts the list and iteratively updates node values to be the sum of all values greater than or equal to the node's original value.
- **Time Complexity**: O(n log n), where `n` is the number of nodes, due to sorting the list of values. DFS is O(n).
- **Space Complexity**: O(n) to store the values and node references.

## 1108.py - Defanging an IP Address
- **Code**: Uses the `replace` method of strings to replace all occurrences of `.` with `[.]`.
- **Time Complexity**: O(n), where `n` is the length of the string.
- **Space Complexity**: O(n), as a new string is created.

## 118.py - Pascal's Triangle
## 119.py - Pascal's Triangle II
- **Code**: Similar approach to Pascal's Triangle (118.py), but only returns the specified row.
- **Time Complexity**: O(n^2), where `n` is `rowIndex`.
- **Space Complexity**: O(n), as it stores the current row being generated.

## 12.py - Integer to Roman
- **Code**: Converts an integer to a Roman numeral by iteratively extracting digits and matching them with a mapping of Roman numeral components (including special cases like 'IV', 'IX', etc.).
- **Time Complexity**: O(1), since the number of digits is small (limited to integers within the range of Roman numerals).
- **Space Complexity**: O(1), for the dictionary.

## 125.py - Valid Palindrome
- **Code**: Cleans the string to keep only alphanumeric characters, converts to lowercase, then uses two pointers from both ends to check for a palindrome.
- **Time Complexity**: O(n), where `n` is the length of the string, due to string cleaning and two-pointer traversal.
- **Space Complexity**: O(n), for the cleaned string.

## 1282.py - Group the People Given the Group Size They Belong To
- **Code**: Uses a dictionary to group indices by their required group size, then iterates through the groups to partition them into lists of the correct size.
- **Time Complexity**: O(n log n), where `n` is the number of people, due to sorting the dictionary keys.
- **Space Complexity**: O(n), to store the grouped indices and the result.

## 13.py - Roman to Integer
- **Code**: Iterates through the string, building combinations to match Roman numeral components (e.g., 'IV') using a dictionary.
- **Time Complexity**: O(n), where `n` is the length of the Roman numeral string.
- **Space Complexity**: O(n), for the dictionary and input list.


- **Code**: Iteratively generates rows of Pascal's triangle. Each row is built based on the previous row by summing adjacent elements.
- **Time Complexity**: O(n^2), where `n` is `numRows`, because we iterate through the triangle elements.
- **Space Complexity**: O(n^2) to store the result triangle.

## 167.py - Two Sum II - Input Array Is Sorted
- **Code**: Uses a dictionary to find the two numbers that sum up to the target, returning their 1-based indices.
- **Time Complexity**: O(n), where `n` is the number of elements.
- **Space Complexity**: O(n), for the dictionary.

## 1672.py - Richest Customer Wealth
- **Code**: Iterates through each customer's accounts and finds the maximum total wealth.
- **Time Complexity**: O(n * m), where `n` is the number of customers and `m` is the number of accounts per customer.
- **Space Complexity**: O(1).

## 1678.py - Goal Parser Interpretation
- **Code**: Iteratively parses the command string using a dictionary to map known patterns ('G', '()', '(al)') to their interpreted values.
- **Time Complexity**: O(n), where `n` is the length of the command string.
- **Space Complexity**: O(n), for the result string.

## 1684.py - Count the Number of Consistent Strings
- **Code**: Checks if each character in a word is present in the allowed characters string.
- **Time Complexity**: O(n * m), where `n` is the number of words and `m` is the average length of a word.
- **Space Complexity**: O(1) (or O(k) where k is the size of the alphabet).

## 169.py - Two Sum
- **Code**: (Note: Code is identical to 1.py) Uses a dictionary to store numbers and their indices to find the pair that sums to the target.
- **Time Complexity**: O(n), where `n` is the number of elements.
- **Space Complexity**: O(n), for the dictionary.

## 17.py - Letter Combinations of a Phone Number
- **Code**: Uses an iterative approach to build combinations of letters for each digit by mapping digits to their corresponding letters.
- **Time Complexity**: O(3^n * 4^m), where `n` is the number of digits that map to 3 letters and `m` is the number of digits that map to 4 letters.
- **Space Complexity**: O(3^n * 4^m), to store the combinations.

## 1720.py - Decode XORed Array
- **Code**: Computes the original array elements by iteratively XORing the previous element with the encoded value.
- **Time Complexity**: O(n), where `n` is the length of the encoded array.
- **Space Complexity**: O(n), to store the decoded array.

## 173.py - Binary Search Tree Iterator
- **Code**: Performs an in-order traversal (DFS) to store nodes in sorted order in an array, then iterates through them.
- **Time Complexity**: O(n) for initialization (DFS), O(1) for `next()` and `hasNext()`.
- **Space Complexity**: O(n), to store the nodes.

## 175.py - Combine Two Tables
- **Code**: Uses dictionaries to join the `Person` and `Address` dataframes by `personId`.
- **Time Complexity**: O(n + m), where `n` and `m` are the number of rows in the tables.
- **Space Complexity**: O(n + m).

## 1757.py - Recyclable and Low Fat Products
- **Code**: Iterates through the dataframe to filter products that are both low fat and recyclable.
- **Time Complexity**: O(n), where `n` is the number of products.
- **Space Complexity**: O(n), for the result.

## 176.py - Second Highest Salary
- **Code**: Collects salaries into a set for unique values, sorts them, and retrieves the second largest.
- **Time Complexity**: O(n log n), due to sorting.
- **Space Complexity**: O(n).

## 1768.py - Merge Strings Alternately
- **Code**: Alternately pops characters from both strings until exhausted.
- **Time Complexity**: O(n + m), where `n` and `m` are the lengths of the strings.
- **Space Complexity**: O(n + m), for the result string.

## 1863.py - Sum of All Subset XOR Totals
- **Code**: Generates all subsets of the array, calculates the XOR sum of each, and returns the total sum.
- **Time Complexity**: O(2^n * n), where `n` is the array length.
- **Space Complexity**: O(2^n * n).

## 187.py - Repeated DNA Sequences
- **Code**: Uses a sliding window of size 10 to extract sequences and counts them in a dictionary.
- **Time Complexity**: O(n), where `n` is the string length.
- **Space Complexity**: O(n).

## 19.py - Remove Nth Node From End of List
- **Code**: Converts the linked list to an array, removes the node, and rebuilds the list.
- **Time Complexity**: O(n), where `n` is the number of nodes.
- **Space Complexity**: O(n).

## 190.py - Reverse Bits
- **Code**: Converts the integer to a 32-bit binary string, reverses it, and converts back.
- **Time Complexity**: O(1) (fixed 32-bit width).
- **Space Complexity**: O(1).

## 191.py - Number of 1 Bits
- **Code**: Converts the integer to a binary string and counts occurrences of '1'.
- **Time Complexity**: O(1).
- **Space Complexity**: O(1).

## 1920.py - Build Array from Permutation
- **Code**: Creates a new array based on the given permutation.
- **Time Complexity**: O(n), where `n` is the array length.
- **Space Complexity**: O(n).

## 1929.py - Concatenation of Array
- **Code**: Concatenates the array with itself.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 199.py - Binary Tree Right Side View
- **Code**: Uses BFS (level-order traversal) and picks the last node of each level.
- **Time Complexity**: O(n), where `n` is the number of nodes.
- **Space Complexity**: O(n).

## 2.py - Add Two Numbers
- **Code**: Converts linked lists to integers, adds them, and converts the result back to a linked list.
- **Time Complexity**: O(n + m), where `n` and `m` are the lengths of the linked lists.
- **Space Complexity**: O(n + m).

## 20.py - Valid Parentheses
- **Code**: Uses a stack to keep track of opening brackets and ensures they are closed in the correct order.
- **Time Complexity**: O(n), where `n` is the length of the string.
- **Space Complexity**: O(n).

## 200.py - Number of Islands
- **Code**: Uses DFS to explore and mark all connected '1's (land) as '0' (visited).
- **Time Complexity**: O(n * m), where `n` and `m` are the dimensions of the grid.
- **Space Complexity**: O(n * m) due to the recursion stack.

## 2011.py - Final Value After Operations
- **Code**: Scans the operations and adjusts the value based on the operation.
- **Time Complexity**: O(n), where `n` is the number of operations.
- **Space Complexity**: O(1).

## 203.py - Remove Linked List Elements
- **Code**: Filters values from the linked list and rebuilds it.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 2044.py - Count Number of Maximum Bitwise-OR Subsets
- **Code**: Generates all subsets, calculates the Bitwise OR, and counts how many subsets have the maximum OR value.
- **Time Complexity**: O(2^n * n), where `n` is the array length.
- **Space Complexity**: O(2^n * n).

## 206.py - Reverse Linked List
- **Code**: Converts the linked list to an array, reverses it, and rebuilds the list.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 177.py - Nth Highest Salary
- **Code**: Similar to 176.py, collects unique salaries, sorts them, and retrieves the nth largest.
- **Time Complexity**: O(n log n).
- **Space Complexity**: O(n).

## 178.py - Rank Scores
- **Code**: Counts occurrences of each score, sorts the scores, and assigns ranks based on the sorted order.
- **Time Complexity**: O(n log n).
- **Space Complexity**: O(n).

## 182.py - Duplicate Emails
- **Code**: Uses a set to track seen emails and identifies duplicates.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).


## 14.py - Longest Common Prefix
- **Code**: Iterates through characters of the first string and checks if they are present at the same index in all other strings.
- **Time Complexity**: O(S), where S is the sum of all characters in all strings.
- **Space Complexity**: O(1) (excluding the space for the result).

## 141.py - Linked List Cycle
- **Code**: Uses a set to store visited nodes. If a node is already in the set, a cycle exists.
- **Time Complexity**: O(n), where `n` is the number of nodes.
- **Space Complexity**: O(n), to store the set of visited nodes.

## 143.py - Reorder List
- **Code**: Stores node values in an array, reorders them, and then updates the linked list in-place.
- **Time Complexity**: O(n), where `n` is the number of nodes.
- **Space Complexity**: O(n), to store the array of values.

## 1431.py - Kids With the Greatest Number of Candies
- **Code**: Finds the maximum number of candies and compares each kid's candies + extraCandies with this maximum.
- **Time Complexity**: O(n), where `n` is the number of kids.
- **Space Complexity**: O(n), for the result list.

## 144.py - Binary Tree Preorder Traversal
- **Code**: Recursive DFS (root, left, right).
- **Time Complexity**: O(n), where `n` is the number of nodes.
- **Space Complexity**: O(n), for the recursion stack and result list.

## 145.py - Binary Tree Postorder Traversal
- **Code**: Recursive DFS (left, right, root).
- **Time Complexity**: O(n), where `n` is the number of nodes.
- **Space Complexity**: O(n), for the recursion stack and result list.

## 1470.py - Shuffle the Array
- **Code**: Splits the array and interleaves the two halves.
- **Time Complexity**: O(n), where `n` is the number of elements.
- **Space Complexity**: O(n), for the result array.

## 148.py - Sort List
- **Code**: Extracts values to an array, sorts it, and then rebuilds the linked list.
- **Time Complexity**: O(n log n), due to sorting.
- **Space Complexity**: O(n), to store the array of values.

## 1486.py - XOR Operation in an Array
- **Code**: Generates the array and computes the XOR of all elements.
- **Time Complexity**: O(n), where `n` is the size of the array.
- **Space Complexity**: O(n), for the array.

## 1512.py - Number of Good Pairs
- **Code**: Counts occurrences of each number in a dictionary and uses combinations to count pairs (nC2).
- **Time Complexity**: O(n), where `n` is the size of the array.
- **Space Complexity**: O(n), for the dictionary.
## 183.py - Customers Who Never Order
- **Code**: Uses dictionaries to map customers to IDs and a set to store ordered customer IDs, then filters customers who didn't order.
- **Time Complexity**: O(n + m), where n and m are the lengths of the tables.
- **Space Complexity**: O(n + m).

## 21.py - Merge Two Sorted Lists
- **Code**: Extracts values from both linked lists into an array, sorts the array, and reconstructs a new linked list.
- **Time Complexity**: O(n log n), where n is the total number of nodes.
- **Space Complexity**: O(n).

## 215.py - Kth Largest Element in an Array
- **Code**: Sorts the array and returns the kth largest element.
- **Time Complexity**: O(n log n).
- **Space Complexity**: O(1) or O(n) depending on sort implementation.

## 2161.py - Partition Array According to Given Pivot
- **Code**: Iterates through the array and separates elements into smaller, equal, and greater lists based on the pivot.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 217.py - Contains Duplicate
- **Code**: Compares the length of the set of the array with the array length to check for duplicates.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 22.py - Generate Parentheses
- **Code**: Uses recursion (backtracking) to generate all combinations of well-formed parentheses.
- **Time Complexity**: O(4^n / sqrt(n)).
- **Space Complexity**: O(n) (recursion depth).

## 2220.py - Minimum Bit Flips to Convert Number
- **Code**: Converts numbers to binary strings, pads them to equal length, and counts differing bits.
- **Time Complexity**: O(n), where n is the number of bits.
- **Space Complexity**: O(n).

## 2235.py - Add Two Integers
- **Code**: Simply adds two numbers.
- **Time Complexity**: O(1).
- **Space Complexity**: O(1).

## 226.py - Invert Binary Tree
- **Code**: Uses recursion to swap left and right children of each node.
- **Time Complexity**: O(n), where n is the number of nodes.
- **Space Complexity**: O(n) (recursion depth).

## 23.py - Merge k Sorted Lists
- **Code**: Collects all values from all lists into an array, sorts them, and reconstructs a new linked list.
- **Time Complexity**: O(N log N), where N is total number of nodes.
- **Space Complexity**: O(N).

## 231.py - Power of Two
- **Code**: Checks if any power of two equals the given number.
- **Time Complexity**: O(1) (fixed range).
- **Space Complexity**: O(1).

## 234.py - Palindrome Linked List
- **Code**: Converts the linked list to a string and checks if it's a palindrome.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 2356.py - Number of Unique Subjects Taught by Each Teacher
- **Code**: Uses a dictionary of sets to count unique subjects for each teacher.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 24.py - Swap Nodes in Pairs
- **Code**: Converts to array, swaps adjacent elements in the array, and rebuilds the linked list.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 2413.py - Smallest Even Multiple
- **Code**: Doubles the number if it's odd to make it even and a multiple of 2.
- **Time Complexity**: O(1).
- **Space Complexity**: O(1).

## 242.py - Valid Anagram
- **Code**: Sorts both strings and compares them.
- **Time Complexity**: O(n log n).
- **Space Complexity**: O(n).

## 2433.py - Find The Original Array of Prefix Xor
- **Code**: Reverses the prefix XOR operation by XORing consecutive elements of the prefix array.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 2469.py - Convert the Temperature
- **Code**: Applies temperature conversion formulas.
- **Time Complexity**: O(1).
- **Space Complexity**: O(1).

## 25.py - Reverse Nodes in k-Group
- **Code**: Converts to array, reverses sub-arrays of size k, and rebuilds the linked list.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 257.py - Binary Tree Paths
- **Code**: Uses DFS to traverse the tree and keep track of paths to leaf nodes.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 2574.py - Left and Right Sum Differences
- **Code**: Calculates prefix and suffix sums and returns the absolute difference.
- **Time Complexity**: O(n), where n is the array length.
- **Space Complexity**: O(n).

## 258.py - Add Digits
- **Code**: Repeatedly sums digits until a single digit remains.
- **Time Complexity**: O(log n).
- **Space Complexity**: O(1).

## 26.py - Remove Duplicates from Sorted Array
- **Code**: Uses a set to remove duplicates, updates the array, and returns the new length.
- **Time Complexity**: O(n log n) due to sorting.
- **Space Complexity**: O(n).

## 268.py - Missing Number
- **Code**: Iterates through the expected range to find the missing number.
- **Time Complexity**: O(n^2) because of `x in nums` (O(n) inside O(n) loop).
- **Space Complexity**: O(1).

## 2695.ts - Array Wrapper
- **Code**: Creates a class to wrap an array and provides custom `valueOf` and `toString` methods.
- **Time Complexity**: O(n), where n is the length of the array.
- **Space Complexity**: O(n).

## 27.py - Remove Element
- **Code**: Uses a two-pointer approach to move elements not equal to `val` to the front.
- **Time Complexity**: O(n).
- **Space Complexity**: O(1).

## 2703.ts - Return Length of Arguments Passed
- **Code**: Returns the length of the arguments array.
- **Time Complexity**: O(1).
- **Space Complexity**: O(1).

## 2723.ts - Add Two Promises
- **Code**: Awaits two promises and returns their sum.
- **Time Complexity**: O(1).
- **Space Complexity**: O(1).

## 2769.py - Find the Maximum Achievable Number
- **Code**: Calculates the maximum achievable number based on the input and allowed operations.
- **Time Complexity**: O(1).
- **Space Complexity**: O(1).

## 2798.py - Number of Employees Who Met the Target
- **Code**: Counts employees whose hours are greater than or equal to the target.
- **Time Complexity**: O(n).
- **Space Complexity**: O(1).

## 28.py - Find the Index of the First Occurrence in a String
- **Code**: Performs a sliding window check for the needle in the haystack.
- **Time Complexity**: O(n * m), where n is haystack length, m is needle length.
- **Space Complexity**: O(1).

## 2807.py - Insert Greatest Common Divisors in Linked List
- **Code**: Extracts values, calculates GCD of adjacent values, and reconstructs the list.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 2879.py - Select First Rows
- **Code**: Returns the first 3 rows of the dataframe.
- **Time Complexity**: O(1).
- **Space Complexity**: O(1).

## 2881.py - Create Bonus Column
- **Code**: Creates a new dataframe with a bonus column.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 2884.py - Modify Salary Column
- **Code**: Creates a new dataframe with a modified salary column.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 2888.py - Reshape Data: Concatenate
- **Code**: Concatenates two dataframes.
- **Time Complexity**: O(n + m).
- **Space Complexity**: O(n + m).

## 2894.py - Divisible and Non-divisible Sums Difference
- **Code**: Calculates the difference between sums of numbers not divisible by `m` and those divisible by `m`.
- **Time Complexity**: O(n).
- **Space Complexity**: O(1).

## 2942.py - Find Words Containing Character
- **Code**: Finds indices of words containing a character.
- **Time Complexity**: O(n * m), where n is number of words, m is max word length.
- **Space Complexity**: O(n).

## 3.py - Longest Substring Without Repeating Characters
- **Code**: Uses a sliding window to find the longest substring without repeated characters.
- **Time Complexity**: O(n).
- **Space Complexity**: O(min(n, m)), where m is alphabet size.

## 3110.py - Score of a String
- **Code**: Sums the absolute differences of ASCII values of adjacent characters.
- **Time Complexity**: O(n).
- **Space Complexity**: O(1).

## 3146.py - Permutation Difference between Two Strings
- **Code**: Maps characters to indices in both strings and sums the absolute differences.
- **Time Complexity**: O(n), where n is the length of strings.
- **Space Complexity**: O(n).

## 3190.py - Find Minimum Operations to Make All Elements Divisible by Three
- **Code**: Calculates operations required to make each number divisible by 3.
- **Time Complexity**: O(n).
- **Space Complexity**: O(1).

## 3211.py - Generate Binary Strings Without Adjacent Zeros
- **Code**: Uses recursion to generate valid binary strings.
- **Time Complexity**: O(2^n).
- **Space Complexity**: O(n) (recursion depth).

## 3280.py - Convert Date to Binary
- **Code**: Splits date, converts components to binary strings, and joins them.
- **Time Complexity**: O(1).
- **Space Complexity**: O(1).

## 3289.py - The Two Sneaky Numbers of Digitville
- **Code**: Uses a dictionary to count frequencies and identifies numbers appearing twice or more.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 33.py - Search in Rotated Sorted Array
- **Code**: Uses Python's list index method to find the element.
- **Time Complexity**: O(n).
- **Space Complexity**: O(1).

## 3300.py - Minimum Element After Replacement With Digit Sum
- **Code**: Replaces each number with its digit sum and finds the minimum.
- **Time Complexity**: O(n * log(max_val)).
- **Space Complexity**: O(n).

## 344.py - Reverse String
- **Code**: Swaps elements using two pointers in-place.
- **Time Complexity**: O(n).
- **Space Complexity**: O(1).

## 3467.py - Transform Array by Parity
- **Code**: Transforms numbers to 0 (even) or 1 (odd) and sorts the array.
- **Time Complexity**: O(n log n).
- **Space Complexity**: O(n).

## 347.py - Top K Frequent Elements
- **Code**: Counts frequencies, identifies the k most frequent elements.
- **Time Complexity**: O(n log n) due to sorting frequencies.
- **Space Complexity**: O(n).

## 3498.py - Reverse Degree Calculation
- **Code**: Calculates a weighted sum based on character values.
- **Time Complexity**: O(n).
- **Space Complexity**: O(1).

## 3512.py - Minimum Operations to Equalize Sum
- **Code**: Calculates necessary operations to reach the target sum based on k.
- **Time Complexity**: O(n).
- **Space Complexity**: O(1).

## 3516.py - Find Closest Element
- **Code**: Compares distances to x and y to find the closest.
- **Time Complexity**: O(1).
- **Space Complexity**: O(1).

## 3541.py - Maximum Frequency Sum
- **Code**: Counts vowels and consonants, sums their maximum frequencies.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 3658.py - GCD of Odd and Even Sums
- **Code**: Calculates sums of even and odd positions and returns their GCD.
- **Time Complexity**: O(n).
- **Space Complexity**: O(1).

## 3668.py - Recover Order
- **Code**: Maps friends to their positions based on the order and reconstructs the order.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 3701.py - Alternating Sum
- **Code**: Calculates alternating sum of elements.
- **Time Complexity**: O(n).
- **Space Complexity**: O(1).

## 3731.py - Find Missing Elements
- **Code**: Identifies numbers missing within the range of elements present in the array.
- **Time Complexity**: O(n log n) or O(n) depending on range size and search.
- **Space Complexity**: O(n).

## 3760.py - Maximum Distinct Characters
- **Code**: Counts distinct characters using a set.
- **Time Complexity**: O(n).
- **Space Complexity**: O(k) (alphabet size).

## 3783.py - Mirror Distance
- **Code**: Reverses the number and calculates the absolute difference.
- **Time Complexity**: O(log n).
- **Space Complexity**: O(log n).

## 3794.py - Reverse Prefix
- **Code**: Reverses the string up to the given index k.
- **Time Complexity**: O(k).
- **Space Complexity**: O(n).

## 3838.py - Map Word Weights
- **Code**: Calculates weighted word values and returns a string based on their modulo 26.
- **Time Complexity**: O(n * m), where n is number of words and m is word length.
- **Space Complexity**: O(n).

## 3898.py - Find Degrees (Graph Nodes)
- **Code**: Counts occurrences of 1s in rows of a matrix.
- **Time Complexity**: O(n * m).
- **Space Complexity**: O(n).

## 39.py - Combination Sum
- **Code**: Uses backtracking to find all combinations summing to target.
- **Time Complexity**: O(2^n).
- **Space Complexity**: O(target).

## 3925.py - Concat With Reverse
- **Code**: Concatenates array with its reversed version.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 3945.py - Digit Frequency Score
- **Code**: Calculates score by summing (digit * frequency).
- **Time Complexity**: O(log n).
- **Space Complexity**: O(1).

## 4.py - Median of Two Sorted Arrays
- **Code**: Combines, sorts, and finds the median.
- **Time Complexity**: O(n log n) due to sorting.
- **Space Complexity**: O(n).

## 46.py - Permutations
- **Code**: Uses backtracking to find all permutations.
- **Time Complexity**: O(n * n!).
- **Space Complexity**: O(n * n!).

## 49.py - Group Anagrams
- **Code**: Groups strings by sorted characters using a dictionary.
- **Time Complexity**: O(n * m log m), where n is number of strings and m is max string length.
- **Space Complexity**: O(n * m).

## 50.py - Pow(x, n)
- **Code**: Uses power operator.
- **Time Complexity**: O(1) or O(log n) depending on implementation of `**`.
- **Space Complexity**: O(1).

## 58.py - Length of Last Word
- **Code**: Splits string by spaces and returns length of last word.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 61.py - Rotate List
- **Code**: Converts to array, rotates by moving last elements to front, and rebuilds list.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 66.py - Plus One
- **Code**: Adds one to the number represented by digits, handling carries.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 67.py - Add Binary
- **Code**: Converts binary strings to integers, adds, and converts back to binary.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 69.py - Sqrt(x)
- **Code**: Iteratively finds the integer square root.
- **Time Complexity**: O(sqrt(x)).
- **Space Complexity**: O(1).

## 7.py - Reverse Integer
- **Code**: Reverses string representation of integer and checks bounds.
- **Time Complexity**: O(log n).
- **Space Complexity**: O(log n).

## 70.py - Climbing Stairs
- **Code**: Uses DP to calculate ways to reach top stair.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 704.py - Binary Search
- **Code**: Performs standard binary search.
- **Time Complexity**: O(log n).
- **Space Complexity**: O(1).

## 705.py - Design HashSet
- **Code**: Uses list to implement set operations.
- **Time Complexity**: O(n) for operations.
- **Space Complexity**: O(n).

## 706.py - Design HashMap
- **Code**: Uses parallel lists to map keys to values.
- **Time Complexity**: O(n) for operations.
- **Space Complexity**: O(n).

## 58.py - Length of Last Word
- **Code**: Strips whitespace, splits the string by spaces, and returns the length of the last word.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 61.py - Rotate List
- **Code**: Converts the linked list to an array of nodes, rotates the array, and reconstructs the list.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 75.py - Sort Colors
- **Code**: Sorts array using nested loops (bubble sort style).
- **Time Complexity**: O(n^2).
- **Space Complexity**: O(1).

## 771.py - Jewels and Stones
- **Code**: Counts occurrences of jewels in stones.
- **Time Complexity**: O(n * m), where n is stones length and m is jewels length.
- **Space Complexity**: O(1).

## 78.py - Subsets
- **Code**: Generates all subsets iteratively.
- **Time Complexity**: O(2^n).
- **Space Complexity**: O(2^n).

## 81.py - Search in Rotated Sorted Array II
- **Code**: Checks if target is in the array.
- **Time Complexity**: O(n).
- **Space Complexity**: O(1).

## 82.py - Remove Duplicates from Sorted List II
- **Code**: Counts occurrences, removes those with >1, and rebuilds list.
- **Time Complexity**: O(n log n).
- **Space Complexity**: O(n).

## 83.py - Remove Duplicates from Sorted List
- **Code**: Removes duplicates and sorts the list.
- **Time Complexity**: O(n log n).
- **Space Complexity**: O(n).

## 88.py - Merge Sorted Array
- **Code**: Merges arrays and sorts.
- **Time Complexity**: O((n+m)^2).
- **Space Complexity**: O(1).

## 9.py - Palindrome Number
- **Code**: Reverses string to check palindrome.
- **Time Complexity**: O(log n).
- **Space Complexity**: O(log n).

## 90.py - Subsets II
- **Code**: Generates all subsets and filters duplicates.
- **Time Complexity**: O(2^n * n log n).
- **Space Complexity**: O(2^n * n).

## 92.py - Reverse Linked List II
- **Code**: Converts to array, reverses sub-segment, and rebuilds list.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 938.py - Range Sum of BST
- **Code**: Performs DFS, sums values within the range.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n) (recursion depth).

## 94.py - Binary Tree Inorder Traversal
- **Code**: Performs DFS in-order traversal.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 66.py - Plus One
- **Code**: Simulates addition by one, handling carries from right to left.
- **Time Complexity**: O(n).
- **Space Complexity**: O(1).

## 67.py - Add Binary
- **Code**: Converts binary strings to integers, adds them, and converts the sum back to a binary string.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 69.py - Sqrt(x)
- **Code**: Uses an iterative approach to find the integer square root.
- **Time Complexity**: O(sqrt(x)).
- **Space Complexity**: O(1).

## 7.py - Reverse Integer
- **Code**: Reverses the digits of an integer, handling negative numbers and overflow.
- **Time Complexity**: O(log x).
- **Space Complexity**: O(log x).

## 70.py - Climbing Stairs
- **Code**: Uses dynamic programming to calculate the number of distinct ways to climb to the top.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 704.py - Binary Search
- **Code**: Implements a standard binary search algorithm.
- **Time Complexity**: O(log n).
- **Space Complexity**: O(1).

## 705.py - Design HashSet
- **Code**: Implements a hash set using a list to store elements.
- **Time Complexity**: O(n) for `add`, `remove`, `contains` in worst case for list-based implementation.
- **Space Complexity**: O(n).

## 706.py - Design HashMap
- **Code**: Implements a hash map using two lists for keys and values.
- **Time Complexity**: O(n) for `put`, `get`, `remove` in worst case for list-based implementation.
- **Space Complexity**: O(n).

