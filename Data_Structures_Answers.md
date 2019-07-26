Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

2. What is the space complexity of your ring buffer's `append` function?

3. What is the runtime complexity of your ring buffer's `get` method?

4. What is the space complexity of your ring buffer's `get` method?


5. What is the runtime complexity of the provided code in `names.py`?
    Runtime complexity of provided code is O(n^2). For each name in the first list, your are looping through every item in the second.

6. What is the space complexity of the provided code in `names.py`?
    Space complexity appears to be O(n). This grows linearly as your duplicates arrary grows.

7. What is the runtime complexity of your optimized code in `names.py`?
    Runtime complexity of optimized code is O(n). The dominant operation in time function is now adding items to the binary tree. Comparisons have been reduced to log(n) which grows slower in the equation: n + log(n)




8. What is the space complexity of your optimized code in `names.py`?
    Space complexity striks me as O(n). As your name lists grow larger so proportionally will the space requirements for reading into lists and reading into the binary tree.
