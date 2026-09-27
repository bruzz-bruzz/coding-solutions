# Codeforces Solutions Explanations

Here are the explanations for the solutions in this folder.

## 1015C.py - Songs Compression
- **Code**: Calculates the difference between original and compressed sizes. Sorts the differences and greedily reduces the total size until it's less than or equal to `m`.
- **Time Complexity**: O(n log n), due to sorting the differences.
- **Space Complexity**: O(n), to store the sizes and differences.

## 1095B.py - Array Stabilization
- **Code**: Sorts the array and removes the largest element. The result is the difference between the new maximum and minimum.
- **Time Complexity**: O(n log n), due to sorting.
- **Space Complexity**: O(n), for the array.

## 110A.py - Nearly Lucky Number
- **Code**: Counts occurrences of '4' and '7' in the input string. Checks if this count is itself a nearly lucky number.
- **Time Complexity**: O(n), where `n` is the number of digits in the input.
- **Space Complexity**: O(n), for storing the input.

## 1141B.py - Cyclic Shifts
- **Code**: Extends the array by concatenating it with itself to handle the cyclic nature and finds the longest sequence of '1's.
- **Time Complexity**: O(n), where `n` is the length of the array.
- **Space Complexity**: O(n), to store the extended array.

## 1360B.py - Honest Coach
- **Code**: Sorts the athletes' strengths and finds the minimum difference between adjacent strengths.
- **Time Complexity**: O(t * n log n), where `t` is test cases and `n` is athletes.
- **Space Complexity**: O(n), to store the strengths.

## 1360C.py - Similar Pairs
- **Code**: Sorts the array and checks if pairs have the same parity or differ by 1.
- **Time Complexity**: O(t * n log n), where `t` is test cases and `n` is array size.
- **Space Complexity**: O(n).

## 146A.py - Lucky Ticket
- **Code**: Checks if all digits are '4' or '7' and if the sums of the first and second halves of the ticket are equal.
- **Time Complexity**: O(n), where `n` is the number of digits.
- **Space Complexity**: O(1).

## 148A.py - Insomnia Cure
- **Code**: Iterates through each day up to `d` and checks if it's divisible by any of the four factors (k, l, m, n).
- **Time Complexity**: O(d).
- **Space Complexity**: O(1).

## 151A.py - Soft Drinking
- **Code**: Calculates the total number of toasts possible based on ingredients and divides by the number of friends.
- **Time Complexity**: O(1).
- **Space Complexity**: O(1).

## 155A.py - I_love_%username%
- **Code**: Iterates through scores, updating min/max to count amazing performances.
- **Time Complexity**: O(n), where `n` is the number of contests.
- **Space Complexity**: O(n), to store the previous scores.
## 158A.py - Next Round
- **Code**: Counts participants who scored at least the k-th place score and have a positive score.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 1873A.py - Short Sort
- **Code**: Compares the input string to the sorted string "abc" and counts differing positions.
- **Time Complexity**: O(1) (fixed length).
- **Space Complexity**: O(1).

## 1873B.py - Good Kid
- **Code**: Sorts array and increments the smallest element to maximize the product.
- **Time Complexity**: O(t * n log n).
- **Space Complexity**: O(n).

## 200B.py - Drinks
- **Code**: Calculates the average of volume percentages.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 228A.py - Is your horseshoe on the other hoof?
- **Code**: Counts distinct colors using a set and subtracts from total.
- **Time Complexity**: O(1).
- **Space Complexity**: O(1).

## 231A.py - Team
- **Code**: Counts questions where at least 2 people agree.
- **Time Complexity**: O(n).
- **Space Complexity**: O(1).

## 34A.py - Reconnaissance 2
- **Code**: Finds the minimum difference between adjacent elements in a circular array and returns their 1-based indices.
- **Time Complexity**: O(n log n) due to sorting by value, then iterating through the array to find positions.
- **Space Complexity**: O(n).

## 381A.py - Sereja and Dima
- **Code**: Players take turns picking the largest available card from either end of the row.
- **Time Complexity**: O(n), where `n` is the number of cards.
- **Space Complexity**: O(n).

## 38A.py - Army
- **Code**: Calculates the total years to pass from year `a` to `b` by summing up `d[i]` values.
- **Time Complexity**: O(b - a).
- **Space Complexity**: O(n), for the array of years.

## 41A.py - Translation
- **Code**: Checks if the first string is the reverse of the second string.
- **Time Complexity**: O(n), where `n` is the length of the string.
- **Space Complexity**: O(n) for reversed string.

## 427A.py - Police Recruits
- **Code**: Simulates police activity, counting untreated crimes.
- **Time Complexity**: O(n).
- **Space Complexity**: O(1).

## 443A.py - Anton and Letters
- **Code**: Uses a set to count unique letters, ignoring non-alphabetic characters.
- **Time Complexity**: O(n).
- **Space Complexity**: O(1) (size of alphabet).

## 49A.py - Queue at the School
- **Code**: Finds the last alphanumeric character and checks if it's a vowel.
- **Time Complexity**: O(n).
- **Space Complexity**: O(1).

## 4A.py - Watermelon
- **Code**: Checks if the weight `w` can be divided into two even parts.
- **Time Complexity**: O(1).
- **Space Complexity**: O(1).

## 509A.py - Maximum in Table
- **Code**: Builds a Pascal's triangle-like table and finds the maximum value.
- **Time Complexity**: O(n^2).
- **Space Complexity**: O(n^2).

## 520A.py - Pangram
- **Code**: Uses a set to check if all 26 lowercase English letters are present in the input string.
- **Time Complexity**: O(n).
- **Space Complexity**: O(1) (size of alphabet).

## 233A.py - Perfect Permutation
- **Code**: Prints a reverse sequence if n is even, else -1.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 236A.py - Boy or Girl
- **Code**: Counts distinct characters; odd implies "IGNORE HIM!", even implies "CHAT WITH HER!".
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 263A.py - Beautiful Matrix
- **Code**: Finds coordinates of '1' and calculates Manhattan distance to the center (2,2).
- **Time Complexity**: O(1) (5x5 matrix).
- **Space Complexity**: O(1).

## 32B.py - Borze
- **Code**: Maps Borze code sequences ('.', '-.', '--') to digits.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

