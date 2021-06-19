# Quicksort
**Divide and Conquer**

There are two point to keep in mind for divide and counquer

- Figure out the base case. Should be the simplest case.
- Divide or decrease your problem unit it becomes the base case

An example of Divide and conquer can be used on a problem where farm land needs to be divided into square boxes that are equal in height and length.

The base case is when the height and width are the same.

To decrease the problem we can figure out the biggest square that can fit then recall the same method to deal with the rest. 

**Quicksort**

Quick sort is an effective algorithm to quickly sort arrays. 

The base case is if the array is of length 0 or 1 the array can be returned as it is already sorted.

To decrease the problem we have two things to think about.

- if the array is of length 2 we can compare the two and swap if need be.
- For anything more than of length 2 we will:
    - Select a random pivot
    - Place everything smaller than the pivot to the left
    - Place everything larger to the right
    - This will then get merged together after calling quicksort on their left and right arrays.
    - There you go sorted. This repeats more if the array is larger.