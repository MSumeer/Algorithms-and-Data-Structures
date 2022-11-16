# TWO CRYSTAL BALL PROBLEM

- Given two crystal balls that will break if dropped from high enough distance,
- determine the exact spot in which it will break in the most optimized way.

This can be achieved by jumping $\sqrt{N}$ instead of a N or $1/2{N}$

Steps:
- We will first find the $\sqrt{N}$ (This will be our jump_length)
- our first for loop will start from the jump_length, end at the end of array and increment by jump_length until the crystal ball breaks
- our seccond for loop will go from $i - jumplength$ up to $i + jump_length$ and will increment by 1 until the crystal ball breaks.
- The floor number where the crystal ball broke in the seccond for loop will be returned otherwise the crystal ball will not break