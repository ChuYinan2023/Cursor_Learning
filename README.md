# Cursor_Learning

## 1. Add Two Numbers (Linked List)

### Problem Description
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.


### Algorithm Analysis
- **Time Complexity**: O(max(m, n))  
  Where m and n are the lengths of the two linked lists. We process each node exactly once.
- **Space Complexity**: O(max(m, n))  
  The length of the new list is at most max(m, n) + 1.

---

## 2. Longest Substring Without Repeating Characters

### Problem Description
Given a string s, find the length of the longest substring without repeating characters.


### Algorithm Analysis
- **Time Complexity**: O(n)  
  Where n is the length of the string. We process each character exactly once.
- **Space Complexity**: O(min(m, n))  
  Where m is the size of the character set (256 for ASCII). We store characters in a hash map.

---


## 3. Median of Two Sorted Arrays

### Problem Description
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.


### Algorithm Analysis
- **Time Complexity**: O(log(min(m, n)))  
  We perform binary search on the smaller array, eliminating half of the remaining elements in each step.
- **Space Complexity**: O(log(min(m, n)))  
  Due to the recursion stack depth, which is logarithmic in the size of the smaller array.

## Test Cases
Both implementations include comprehensive test cases covering:
- Basic examples
- Edge cases (empty input, single character)
- Large inputs
- Special characters and numbers