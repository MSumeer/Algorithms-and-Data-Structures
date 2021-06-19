Binary search is an algorithm; its input is a sorted list of elements. If the element is in that list, binary search returns the position where it's located. Otherwise binary search  returns null. 

## **How does Binary search work?**

Think of a number between 1 and 100. Guess the number in the fewest amount of tries possible. For every guess you will find out if your guess is too high, too low or correct.

Binary search will start with the median index in this case 50.

- 50? Too low

Yes the number is too low but you eliminated every number ≤ 50. Next guess between 50 and 100 = 75.

- 75? Too high

Yes the number is too high however now numbers that are ≥ 75 are eliminated. Now the next guess will be the median of 50 and 75 = 63. This carries on until correct or not found.

- 63? Too High
- 57? Correct!

If you have 100 items you can find the item in a maximum of 7 times as shown below:

- 100 → 50 → 25 → 13 → 7 → 4 → 2 → 1

If you had a phone book with 240k entries. How many steps would it take in the worst case to find the item for a naive search vs binary search.

- **Naive Search -** Worst case would 240k steps if the entry being searched was the last entry
- **Binary Search -** Would take 18 steps as shown below
    - 240k → 120k → 60k → 30k → 15k → 7.5k → 3750 → 1875 → 938 → 469 → 235 → 118 → 59 → 30 → 15 → 8 → 4 → 2 → 1

## **Big O notation**

Naive Search → $O(n)$

Binary Search →$O(\log_{2}n)$