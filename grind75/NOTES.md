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

## Merge Two Sorted Lists

This problem demonstrates the use of a linked list. It was somewhat troublesome for me in Python, but the key takeaway is to advance the pointer only once at a time.  
Don’t try to do two additions to the list simultaneously. Creating a head node is fine, but **keep the head**. Even if the head’s value isn’t needed, it’s important to maintain it so that the linked list construction remains simple and valid.  
If the head value isn’t needed, just return `head.next`.

```python
while list1 is not None and list2 is not None:
    if list1.val <= list2.val:
        list3.next = list1
        list3 = list3.next
        list1 = list1.next
    else:
        list3.next = list2
        list3 = list3.next
        list2 = list2.next
```

## Best Time to Buy and Sell Stock

This problem demonstrates the **sliding window** technique.

**Requirements:**
- There must be a constraint that you *must buy before you sell* for this approach to work.
- Always assume the first element is the lowest.
- As you iterate through the array (list in Python), if you find a new minimum, set that as the new `min`.
- If the current value is not less than `min`, subtract it by the `min` and track the difference.
- If that difference is ever greater than the current maximum, replace the maximum with it.

In essence, you’re keeping track of two values—`min` and `max profit`—and sliding them along the array, updating as needed.
