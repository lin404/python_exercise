### 001
Binary Tree

### 002
Latest recently use (LRU) // TODO

### 003
Median of Two Sorted Arrays

### 004
Convert Sorted Array to Binary Search Tree
// operator // -> int()

### 005
Binary Search Tree Iterator

### 006
Maximum Binary Tree
> Time complexity -> O(logN) or O(N^2)

### 007
Merge k Sorted Linked-Lists
> Time complexity -> O(N) + O(logN)*O(N) = O(NlogN)

### 008
Add Two Numbers (linked-list)

### 009
K Closest Points to Origin
> sort(), sorted(), lambda

### 010
Best Time to Buy and Sell Stock III // TODO

### 011
Longest Palindromic Substring

### 012
Number of Islands
> DFS (Depth First Search for a Graph)

### 013
Max Area of Island
> DFS

### 014
Trapping Rain Water
> Dynamic Programming (use 2 pointers)

### 015
Product of Array Except Self
> range(n-1, -1, -1) -> reversed(range(n))

### 016
Remove Linked List Elements

### 017
Flatten Binary Tree to Linked List // TODO

### 018
Remove Nth Node From End of Linked List

### 019
Reverse Linked List

### 020
Invert(Reverse) Binary Tree

### 021
Merge Two Sorted Lists

### 022
Maximum Product of Three Numbers
> try O(N)

### 023
Top K Frequent Words
> collections.Counter(); heapq.heapify()/heapq.heappop()
> sort with multiple keys

### 024
Flower Planting With No Adjacent

### 025
Letter Tile Possibilities
> itertools.permutations()

### 026
License Key Formatting

### 027
Balanced Binary Tree
> check depth for each node

### 028
Unique Binary Search Trees

### 029
Serialize and Deserialize Binary Tree

### 030
Merge intervals

### 031
Minimum Window Substring

### 032
Fruit Into Baskets // TODO

### 033
Evaluate Division

### 034
K Empty Slots // TODO

### 035
Longest Absolute File Path // TODO

### 036
Course Schedule II // TODO

### 037
3Sum // TODO

### 038
Meeting Rooms II // TODO

### 039
Next Closest Time // TODO

### 040
Find the Town Judge

### 041
Longest Substring Without Repeating Characters

### 042
Meeting Rooms II
> Heap Data Structure

### 043
Top K Frequent Elements
> Heap Data Structure

heapq.nlargest:
key=str.lower Equivalent to: sorted(iterable, key=key, reverse=True)[:n]

heapq.nsmallest:
key=str.lower Equivalent to: sorted(iterable, key=key)[:n]

sorted(dict.keys(), key=lambda k: dict[k])  -->  sorted(dict.keys(), key=dict.get)