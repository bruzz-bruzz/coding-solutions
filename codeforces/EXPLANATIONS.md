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
## 546A.py - Soldier and Bananas
- **Code**: Calculates the total cost of bananas and returns the amount borrowed, if any.
- **Time Complexity**: O(w).
- **Space Complexity**: O(1).

## 59A.py - Word
- **Code**: Counts uppercase and lowercase letters; converts the word to the majority case.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 617A.py - Elephant
- **Code**: Greedily subtracts 5, 4, 3, 2, or 1 to reach 0 steps.
- **Time Complexity**: O(n).
- **Space Complexity**: O(1).

## 61A.py - Ultra-Fast Mathematician
- **Code**: XORs two binary strings by comparing characters at each index.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 630A.py - Again Twenty Five!
- **Code**: Prints 25 (the result of 5^n mod 100 for n >= 2).
- **Time Complexity**: O(1).
- **Space Complexity**: O(1).

## 630C.py - Lucky Numbers
- **Code**: Calculates the total number of lucky numbers of length up to n.
- **Time Complexity**: O(n).
- **Space Complexity**: O(n).

## 677A.py - Vanya and Fence
- **Code**: Counts total width needed, accounting for taller people taking 2 units of width.
- **Time Complexity**: O(n).
- **Space Complexity**: O(1).

## 681A.py - A Good Contest
- **Code**: Checks if any participant had a rating >= 2400 before and increased their rating after.
- **Time Complexity**: O(n).
- **Space Complexity**: O(1).

## 688A.py - Opponents
- **Code**: Tracks the longest streak of days where at least one opponent was not present.
- **Time Complexity**: O(d * n).
- **Space Complexity**: O(1).

## 703A.py - Mishka and Game
- **Code**: Simulates a game between Mishka and Chris, comparing scores each round.
- **Time Complexity**: O(n).
- **Space Complexity**: O(1).

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


### 705A.py
- **Code Explanation**: Uses a dictionary to toggle between 'I hate' and 'I love' for each layer, appending 'that' between layers and 'it' at the end.
- **Time Complexity**: O(n), where n is the input number.
- **Space Complexity**: O(n) to build the result string.

### 732A.py
- **Code Explanation**: Simulates the number of shovels bought (starting from 1) until the total cost ends in 0 or matches the coin value `r`.
- **Time Complexity**: O(1), as it checks at most 10 possibilities.
- **Space Complexity**: O(1).

### 734A.py
- **Code Explanation**: Counts the occurrences of 'A' and 'D' in the input string and compares the counts to determine the winner.
- **Time Complexity**: O(n), where n is the length of the string.
- **Space Complexity**: O(1).

### 734B.py
- **Code Explanation**: Maximizes the sum by first taking as many "256" combinations as possible using available '2', '5', and '6' counts, then using remaining '2' and '3' for "32" combinations.
- **Time Complexity**: O(1).
- **Space Complexity**: O(1).

### 746A.py
- **Code Explanation**: Iterates through the number of possible compote sets (1 part lemon, 2 parts apple, 4 parts pear) and finds the maximum valid number of sets.
- **Time Complexity**: O(min(lemons, apples/2, pears/4)).
- **Space Complexity**: O(1).

### 750A.py
- **Code Explanation**: Calculates available time after the travel to the contest, then simulates the time required to solve problems 1 through `n`, counting how many can be solved within the limit.
- **Time Complexity**: O(n).
- **Space Complexity**: O(1).

### 758A.py
- **Code Explanation**: Identifies the maximum welfare value among all citizens and calculates the total welfare needed to bring everyone to that maximum.
- **Time Complexity**: O(n).
- **Space Complexity**: O(1).

### 764A.py
- **Code Explanation**: Generates lists of time points when the two artists paint (multiples of their respective periods) up to `z`, and then counts the common points.
- **Time Complexity**: O(z/n + z/m).
- **Space Complexity**: O(z/n + z/m).

