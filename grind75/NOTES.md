## Two Sum

The key takeaway from this problem was understanding two possible solutions:
- Using a nested loop for `O(n²)` search time.
- Using a hash map for `O(n)` complexity.

I did some research into how hash maps work:
- **Hash maps** use a hashing algorithm to store values based on key–value pairs, giving `O(1)` average search time.
- The key’s memory location is determined by computing something like `hash(10)`.  
  When a `10` is encountered again, `hash(10)` is recomputed.  
  If the value already exists, it’s reused; otherwise, it’s stored.
