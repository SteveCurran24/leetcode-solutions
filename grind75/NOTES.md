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

- To adjust the lowpoint to the mid, low becomes → `low = mid + 1`  
- To adjust the highpoint to the mid, high becomes → `high = mid - 1`  
- Midpoint calculation → `mid = (low + high) // 2`

This sliding of low and high progressively halves the search space, giving O(log n) time complexity and discarding useless values.

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

## Linked List Cycle
This problem was another sliding pointer problem. This time, it was using an Algorithm called "Floyd's Algorithm", where one pointer moves faster than the next. If they meet, it's a loop. It also reinforced work with linked lists. The hardest part was understanding how to traverse the linked list in a clear way that would fail at appropriate times.
[**Floyd's Cycle Finding Algorithm – GeeksforGeeks** – Documentation on Floyd's Cycle Finding Algorithm](https://www.geeksforgeeks.org/dsa/floyds-cycle-finding-algorithm/)

## Implement Queue using Stacks

This problem demonstrates the difference between a queue and a stack, specifically Fifo vs Filo. You can leverage two stacks by filling one, and popping and pushing into another. This way it reverses the order of the stack and the second stack effectively becomes the Queue. 
 - Fill one stack, this will be First in, Last out
 - Pop from stack one while pushing into stack two
 - Pop from stack two after its full
 - This will simulate First in First out.


## First Bad Version
This was another example of Binary search with a slight caveat. This was more about finding the boundary, rather than the specific value, which changed the logic slightly. The key was still to use low mid and high values, search, and discard the left or right side of the dataset. The difference however, was in how we updated the boundaries. If mid WAS in the range, we wanted to keep it included rather than discard it like in the value search. 

 - if isBadVersion(mid):  <-- this means that mid IS part of the failed subset, so it could be the version we're looking for.
 - because of this, we move high to that point. In the classic binary search problem we removed that
 - high = mid versus high = mid - 1

The other nuanced difference is, while low < high: rather than while low < = high. When searching for a specific element, you need to be certain that you have covered everything, meaning you need to check when low == high. When checking for a turning point, you will eventually achieve that low = high naturally by just searching less than.


## Climbing Stairs
The climbing stairs problem was an example of dynamic programming. Basically "Can this problem be broken into smaller problems that overlap and combine to form a solution". This was tough for me to understand but after some reading, dynamic programming is effectively just an optimization technique used to make recursion a bit better by increasing efficiency. With recursion, you are brute forcing every solution. If f(3) needs to be calculated, recursion calculates it each and every time unless you keep track of states (ie using the optimization method of DP). With Dynamic programming, you keep track of that state and don't re-solve. Dynamic programming can be done with recursion OR with iteration (using a for / while loop)

[**Dynamic Programming or DP** – Documentation on Dynamic Programming](https://www.geeksforgeeks.org/competitive-programming/dynamic-programming/)

I worked towards making a solution for the traveling salesman problem that illustrates this with a little more depth. [Link to that problem](https://github.com/SteveCurran24/practice-problem-solutions/blob/main/math-based-solutions/taveling-salesman-solver.py)

## Longest Palindrome
This problem was about figuring out the rules behind forming a palindrome. Originally, I had a bunch of if/else statements trying to handle every case, but the logic is actually straightforward:
 - If there are odd-count letters, exactly one can be used as the center.
 - Every other odd count can contribute up to (count - 1) (to make it even).
 - Even counts can be used entirely.

## Reverse a Linked List
This was tough to visualize. Execution was strait forward, but coding was tripping me up. I found a great video from "NeetCode" that walked me through. The explanation of how to move the pointers was enough to get me over the finishline. The key is just keeping track of moving pointers throughout a linked list. 
[Reverse Linked List](https://www.youtube.com/watch?v=G0_I-ZF0S38&t=1s)

## Majority Element
Originally I solved this with a dictionary. Because that potentially copies the entire input, it becomes O(n) space. I followed the challenge to write it with linear time, and constant (O(1)) space. This requires a few passes. and leverages the [Boyer-Moore Majority voting algorithm](https://www.geeksforgeeks.org/theory-of-computation/boyer-moore-majority-voting-algorithm/). The idea is effectively that the majority value will always outpace any minority value. The second pass is to confirm that it fulfills the criteria n/2


## Add Binary
This problem taught me a few really solid tricks that I can potentially reuse in the future. First and foremost the overal logic behind the problem is incredibly straitforward. Typical binary addition rules apply, startin from the right-most digits. The tricks I learned / realized were relevant here:
 - Leveraging a while loop to trace through the strings individually. 
   - This allowed for better time complexity when compared to O(n^2) that nested loops would cause, and it was much simpler to visualize / code.
 - Using %2 and //2.
   - This was so helpful. I didn't put together the simpe logic of 1 + 0 = 1, 1 + 1 causes a remained but still = 0. I knew those rules for binary addition, but using division and modulo to handle the carry made it unbelievably easy.
 - Using x = int(a[i]) if i >= 0 else 0 and y = int(b[j]) if j >= 0 else 0 were very simple ways to account for unequal length strings.
   - Those values just become 0 when out of bounds. That's the key.  
 - with the code, it is more efficient to build it backwards, and then reverse it. Alternatively you can "append to the front" but I believe that costs more overhead.
 - Python join is potent here and will be a staple. Strings are immutable in python, so the cost overhead is exponentially high if you appent to a string over and over. It creates a new string each time.
 - The math was significantly better. Originally I had considered creating massive if else statements but that was definitely the incorrect approach.

## Diameter of Binary Tree
This is a deeper version of the Height of a tree, where you just get two heights and compare them for distance. The key takeaway was the pseudo global variable in python, the use of an accumulation variable.
 - Diameter needs to be calculated at every node. In some circumstances, the root is not part of the overall longest route.
 - I ran a helper function to return the height and leveraged the accumulator to track diamter, only returning diamter from the main function
 - Because it is DFS, it is O(n) complexity.

## Middle of the Linked List
I was able to use the slow/fast pointer trick so solve this one. I advance one pointer at a rate faster than the other. When the faster pointer hits the end, the first pointer is at the midway point. Syntatically it was tricky because I had to track the correct location of NULL values for the faster pointer. Overall it took about 10 minutes to solve. 

## Contains Duplicate
I used a loop with a dictionary to keep track of values as I went. If the value was ever in the dictionary, it would immediately return True. Otherwise it makes it through the array and returns False. This is worst case O(n) as it will only ever progress through the data once, and it is necessary to evaluate every entry in the array. 

## Max Subarray
The idea here is to search through the array. If adding the current best to the next number, would be GREATER than the next number, than that's good. We only ever care about increasing our total. If adding the current best to the next number would be smaller than just taking the next number, we're going to discard everything before. With that outcome, even if it's just a single element, that larger value in the array becomes the largest sub array, so we don't care about anything before it. 

## Insert Interval
Compare the new interval values to the existing in a loop:
 - if newInterval[0] > interval[1] - This means that the new interval lies completely to the right of the existing one, for example new interval = (5,6) existing = (1,2) 5 > 2, so the elements in order become (1,2), (5,6)
   - In this case we just append the existing to our new list. and continue analyzing with our existing "new interval". This inherantly sorts the list.  
 - if newInterval[1] < interval[0] - This means that the new interval lies completely to the left of the existing. For example new interval = (1,3) existing = (5,6). Because 3 < 5 the result is (1,3) (5,6)
   - In this case, we append the newInterval, (placing it before the existing in the new array we're creating) the we set newInterval to interval to continue building the new list. (We could also break the array and just append the entire rest of the list, because it is ensured that the rest will be sorted. 
 - Otherwise the values need to be merged. By setting the new interval bounds to the min of the two first elems, and the max of the two second elems, the elements are effectively being combined thus removing any overlap. Eventually the conditions from above will be met, and the rest of the list will be created.
 - Finally, we append the newInterval, which is effectively just the last value created by the elif portion of the if statement inside of the loop
