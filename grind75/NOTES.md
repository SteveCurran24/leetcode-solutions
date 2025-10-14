# LeetCode Notes

> **Note:** These are my personal notes for my own quick reference and learning.  
> They’re informal, written in my own words, and focus on what *I* found important while solving each problem.

---

## Two Sum

The key takeaway from this was using either a nested loop for **O(n²)** search time, or a **hash map** for **O(n)** complexity.  
I did some research into how hash maps work.  

- **Hash maps** – Hashing algorithm used to store values based on key pairs (**O(1)** search time).  
  The key location in memory is stored at `hash(10)`. When a `10` is encountered again, `hash(10)` is computed.  
  If the value is there, it is left alone; if it is not, it is stored.  

---

## Valid Parentheses

This illustrates the use of a stack in Python — a list has all of the functionality of a stack.  
You use `.append` for push and `.pop` for pop.  

- I created a dictionary to store the keypairs, and the "reverse" order.  
  Meaning that I set the closing bracket values to be the key, so that when I pop I can just verify the dictionary correctly.  

For example:  
If I encounter `}`, I will pop. I will then take the `}` that I encountered and use that to look up the other side of it in the dictionary.  
Because I assigned the value `{`, if what I popped equals `{` then it's good; else, fail.  
Also fail if the stack is empty.

---

## Merge Two Sorted Lists

This demonstrates the use of a linked list. Troublesome for me in Python, but the key takeaway is to only advance the pointer one at a time.  
Don't try to do two additions to the list at the same time. Also, creating a head is fine, but I want to **keep** the head.  
Even if I don't need the value at the head, it's important to keep it so that construction of the linked list remains valid and simple.  
If I don't need the head value, just return `head.next`.

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

- The above code illustrates only advancing the pointer for `list1` and `list3` or `list2` and `list3` by one step.  
- Don't forget to add the rest of a list if one of the lists empties (for non-equivalent list lengths).

---

## Best Time to Buy and Sell Stock

This problem demonstrates the **sliding window** theory.

**Requirements:**
- Must have a constraint of "must buy before sell" for this theory to work.  
- Always assume the first element is the lowest.  
- As you work through the array (list in Python), if you find a new minimum, set that to `min`.  
- If it's not less, subtract the value with the minimum and keep track.  
- If that is ever a larger number, replace the maximum with it.  

I am effectively just keeping track of two values and sliding them along the array, replacing as needed.

---

## Valid Palindrome

It appears that the point of this problem is to actually just keep track of two moving pointers.  

[**Two Pointers Technique – GeeksforGeeks** – Documentation on Two Pointers technique](https://www.geeksforgeeks.org/dsa/two-pointers-technique/)

- You `letter.lower().alnum()` each letter starting from the left and starting from the right, and compare them to the middle.  
- When running this code, because strings are immutable, I opted to run everything in a list so that I wouldn't have to append to the string. Appending to a string in Python is **O(n²)**.  
- If you sanitize first, the space complexity becomes **O(n)**, but if you sanitize on the fly, the space complexity is **O(1)**.

---

## Invert Binary Tree

The point of the problem was to practice recursion. Straightforward enough — if `root` is `None`, return to stop it from looping forever.  
Call the code on the left all the way to the bottom, then call it on the right.  
After there are none left, it will return out and just swap each node.  

The trickiest part was understanding the Python syntax.

---

## Valid Anagram

The point was to just employ a hash map.  
You count the letter frequency in the first string and make sure it matches in the second.  
Otherwise, it fails.

---

## Binary Search

This is a straightforward binary search. Initially, I was trying to use recursion, but that did not work because I was losing the index (which you need to return).

Eventually, I settled on a **while loop**. While the low point and high point are not equal (and the low is less than the high), take the midpoint and see if the target is in the upper half or the lower half, and recalculate the midpoint appropriately.

**Key logic:**

- Left becomes → `high = mid - 1`  
- Right becomes → `low = mid + 1`  
- Midpoint calculation → `mid = (low + high) // 2`

---

## Flood Fill

The point of the problem was to employ the **DFS algorithm** to traverse a 2D array.  
The portion that I stumbled with was twofold:

- **I was returning prematurely.**  
  I put too many returns in because I was too rigid in my mindset.  
  The goal was to traverse to the bounds and then effectively return to the start point.  
  I needed to just allow the flow of the algorithm naturally.  

  For example:

  ```
  if up
      do logic
  if down
      do logic
  if left
      do logic
  if right
      do logic
  ```

  **NOT**

  ```
  if up
      do logic
  else
      return
  ```

  etc.

- **I did not consider the inclusion of zero** in the length of the array.  
  When doing a check against `len(image)`, I need to make sure to subtract 1 because of **0 inclusivity**.  
  Silly mistake.

  ---
## Lowest Common Anscestor

This problem was to illustrate the use of a Binary Search Tree. I immediately recognized that if the node was a split, that was the answer. 
  ```
  if p is < node and q is > node
    answer is node
  ```

I initially solved it with recursion, but the efficiency was on the low end compared to other solutions, so I re-wrote the code using a while loop for traversal. That increased the efficiency quite a bit. The Key takeaway is just BST traversal. 

## Balanced Binary Tree
The problem overall is to track recursion. This problem was a large challenge because I was struggling to understand what values actually needed to be tracked / returned, but settled on tracking a single total height, and returning a -1 if the subtree was imbalanced.

- If the root is NULL, return 0, there is no additional height
- recursively call left. If left height ever equals -1, it means that the left subtree is imbalanced and the code is safe to return -1 all the way out
- recursively call right. Same as left, if its ever equal to -1 it is imbalanced
- if the absolute value of left height minus right height is ever greater than 1 (ie imbalanced) return -1
- otherwise return 1 plus whichver height is larger at that moment.

These math for balance is done in each individual recursive call on each subtree, and only the total height is tracked. If it ever becomes -1, it means the tree is imbalanced and it is safe to return all the way to to root.













