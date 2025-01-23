# ZeroDivisionError in Python

This repository demonstrates a common Python error: `ZeroDivisionError`. The `bug.py` file contains code that attempts to divide by zero, causing the error. The `bugSolution.py` file provides a solution by incorporating error handling to gracefully manage this scenario.

## Bug Description
The `my_function` in `bug.py` does not handle the case where the denominator `b` is zero. This results in a `ZeroDivisionError` when the function is called with `b = 0`.

## Solution
The solution in `bugSolution.py` uses a `try-except` block to catch the `ZeroDivisionError`. If the error occurs, an appropriate message is printed; otherwise, the division proceeds normally.