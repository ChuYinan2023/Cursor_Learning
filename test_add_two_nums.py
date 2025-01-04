# importing the add-two-nums.py file
from add_two_nums import ListNode, Solution

def create_linked_list(lst):
    """Helper function to create a linked list from a list of digits"""
    dummy = ListNode()
    current = dummy
    for digit in lst:
        current.next = ListNode(digit)
        current = current.next
    return dummy.next

def print_linked_list(l):
    """Helper function to print a linked list"""
    result = []
    while l:
        result.append(str(l.val))
        l = l.next
    print(' -> '.join(result))

def main():
    # Test cases
    test_cases = [
        ([2, 4, 3], [5, 6, 4]),  # Example 1
        ([0], [0]),              # Example 2
        ([9,9,9,9,9,9,9], [9,9,9,9]),  # Example 3
        ([1,8], [0]),            # Different lengths
        ([5], [5]),              # Single digit with carry
        # New complex test cases
        ([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [5,6,7]),  # Very long number + short number
        ([9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9], [1]),      # All 9s + 1
        ([1], [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]),    # 1 + very long number of 9s
        ([6,5,4,3,2,1], [1,2,3,4,5,6]),                       # Same length, no carry
        ([9,9,9,9,9,9,9,9,9,9], [9,9,9,9,9,9,9,9,9,9]),       # Two large numbers with carry
        ([1,0,0,0,0,0,0,0,0,0,1], [9,9,9,9,9,9,9,9,9,9]),     # Edge case with carry propagation
    ]
    
    solution = Solution()
    
    for l1_digits, l2_digits in test_cases:
        l1 = create_linked_list(l1_digits)
        l2 = create_linked_list(l2_digits)
        
        print("Input:")
        print_linked_list(l1)
        print_linked_list(l2)
        
        result = solution.addTwoNumbers(l1, l2)
        
        print("Output:")
        print_linked_list(result)
        print("-" * 30)

if __name__ == "__main__":
    main()