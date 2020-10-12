#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n^3) because n is being multiplied three times


b) O(n log n) because there are two loops and one is a subset of the other


c) O(n) because we do exactly one operation for each bunny

## Exercise II

Since our floors are sorted and ordered we can utilize a binary search. Therefore we will achieve a O(log n) runtime

    # split the floors. take the middle
        # 1 -> middle - 1 on the left / middle -> last on the right
    # guess / toss egg
    # if the egg breaks
        # cut left set of floors in half, take the middle, try again
    # if the egg does not break
        # cut right set of floors in half, take the middle, try again
