## Two Sum

The key takeaway from this problem was understanding two possible solutions:
- Using a nested loop for `O(n²)` search time.
- Using a hash map for `O(n)` complexity.

I did some research into how hash maps work:
- **Hash maps** use a hashing algorithm to store values based on key–value pairs, giving `O(1)` average search time.
- The key’s memory location is determined by computing something like `hash(10)`.  
  When a `10` is encountered again, `hash(10)` is recomputed.  
  If the value already exists, it’s reused; otherwise, it’s stored.

## Valid Parentheses

This problem illustrates the use of a stack in Python. A list provides all of the functionality of a stack, using `.append()` for push and `.pop()` for pop operations.

- I created a dictionary to store the key–value pairs in *reverse* order, meaning that closing brackets are used as keys.  
  This allows direct verification when popping from the stack.

For example:  
If I encounter `}`, I pop from the stack. Then, I take the `}` and look up its corresponding opening bracket in the dictionary.  
If what I popped equals `{`, the match is valid. Otherwise, it fails.  
The function also fails if the stack is empty when attempting to pop.

