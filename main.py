"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        ra = foo(x - 1)
        rb = foo(x - 2)
        return ra + rb

def longest_run(mylist, key):
    """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the length of the longest continuous sequence of `key` in `myarray`
    """
    max_count = 0  # Stores the longest sequence found
    count = 0  # Tracks current streak of `key`

    for num in mylist:
        if num == key:
            count += 1
            max_count = max(max_count, count)  # Update max streak
        else:
            count = 0  # Reset streak if key is broken

    return max_count




class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(myarray, key):
    """
    A recursive, divide and conquer implementation to find the longest contiguous run of `key`.

    Args:
      myarray (list): List of integers.
      key (int): The target value.

    Returns:
      int: The length of the longest contiguous sequence of `key`.
    """
    if not myarray:
        return 0  # Edge case
    
    if len(myarray) == 1:  # Base case
        is_key = (myarray[0] == key)
        return Result(1 if is_key else 0, 1 if is_key else 0, 1 if is_key else 0, is_key)

    # Split into left and right halves
    mid = len(myarray) // 2
    left_result = longest_run_recursive(myarray[:mid], key)
    right_result = longest_run_recursive(myarray[mid:], key)

    # Compute the longest cross-run 
    cross_run = 0
    if myarray[mid - 1] == key and myarray[mid] == key:
        cross_run = left_result.right_size + right_result.left_size

    # Compute longest run found
    longest_size = max(left_result.longest_size, right_result.longest_size, cross_run)

    # Compute left_size
    left_size = left_result.left_size
    if left_result.is_entire_range and myarray[mid] == key:
        left_size += right_result.left_size

    # Compute right_size (longest run ending at rightmost element)
    right_size = right_result.right_size
    if right_result.is_entire_range and myarray[mid - 1] == key:
        right_size += left_result.right_size

    # if the entire segment consists of `key`
    is_entire_range = left_result.is_entire_range and right_result.is_entire_range

    return Result(left_size, right_size, longest_size, is_entire_range)
