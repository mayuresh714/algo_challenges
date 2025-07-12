# Optimise Multiplication

This challenge is about finding efficient ways to multiply numbers, exploring different algorithms and optimisations. The goal is to understand how multiplication can be performed under various constraints and how complexity can be reduced in real-world scenarios.

Feel free to contribute your own approaches or insights! 💡

# Multiply Two Integers Using Custom Operations


## 📘 Problem Description

Implement a function `multiply(a, b)` that multiplies two non-negative integers `a` and `b` without using `*`, `//`, or `%` operators. **Note:** Both `a` and `b` will always be non-negative integers, and you cannot use negative integers to simulate subtraction or for any other purpose.

You are provided with the following helper functions:

```python
def add(x, y):
    # Returns the sum of x and y
    return x + y

def isequal(x, y):
    # Returns True if x is equal to y, otherwise False
    return x == y

def islessthan(x, y):
    # Returns True if x is less than y, otherwise False
    return x < y
```

You must use these helper functions to build the `multiply(a, b)` function.

## 🔧 Function Signature

```python
def multiply(a: int, b: int) -> int:
    # Your code here
```

## ✅ Constraints

- `0 <= a, b <= 10^1000`
- You must not use the `*`, `//`, or `%` operators.
- You must only use the helper functions provided (`add`, `isequal`, `islessthan`) for performing arithmetic or comparisons.
- You may use assignment (`=`), if/else conditions, and function calls, but no other arithmetic, bitwise, or comparison operators (including `-`, `^`, binary ops, etc.).
- You cannot use negative integers to simulate subtraction or for any other purpose.

## 💡 Example

```python
Input: a = 3, b = 4  
Output: 12

Input: a = 0, b = 99  
Output: 0

Input: a = 7, b = 1  
Output: 7
```

## 🧠 Follow-up

Can you optimize your implementation to run faster than linear time?

---

**Special Note:**
This problem already ensures that only non-negative integers are provided for multiplication, and the constraints above strictly prohibit the use of any operators other than assignment and control flow. You must only use the provided helpers for all arithmetic and comparisons. Negative integers cannot be used for any purpose, including simulating subtraction.
