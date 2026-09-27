# AtCoder Solutions Explanations

## ABC476_A.py
- **Code**: Appends 'r' to the input string if it ends with 'e', otherwise appends 'er'.
- **Time Complexity**: O(n), where n is the length of the string.
- **Space Complexity**: O(n) to store the result.

## ABC476_B.PY
- **Code**: Compares two strings character by character, ignoring positions with '*' in the second string.
- **Time Complexity**: O(n), where n is the length of the strings.
- **Space Complexity**: O(1).

## ABC476_C.PY
- **Code**: Maintains a min-heap of size 3 to track the 3rd smallest element as we iterate through the array.
- **Time Complexity**: O(n log 3) = O(n).
- **Space Complexity**: O(1) (heap size is constant 3).

## ABC477_A.PY
- **Code**: Uses a dictionary to map colors in a cycle ('B' -> 'Y', 'Y' -> 'R', 'R' -> 'B').
- **Time Complexity**: O(1).
- **Space Complexity**: O(1).

## ABC477_B.PY
- **Code**: Compares each element with all other elements to check if all absolute differences are at least `d`.
- **Time Complexity**: O(n^2), where n is the number of elements.
- **Space Complexity**: O(n) to store the results.

