#!/usr/bin/python3
"""
This script defines a function to find a peak element in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    """
    Find a peak element in a list of integers using binary search.

    Args:
        list_of_integers (list): The list of unsorted integers.

    Returns:
        int or None: The peak element found in the list or None if the list is empty.

    This function uses a binary search algorithm to efficiently find a peak element in
    the given list. It starts with two boundaries, left and right, and iteratively
    narrows down the search range until a peak element is found.
    """
    # Check if the input list is empty
    if not list_of_integers:
        return None

    # Initialize left and right boundaries for binary search
    left, right = 0, len(list_of_integers) - 1

    # Perform binary search to find a peak element
    while left < right:
        # Calculate the middle index
        mid = (left + right)

        # Compare the middle element with the element to its right
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1  # If the right element is greater, move the left boundary
        else:
            right = mid  # If the middle element is greater, move the right boundary

    # Return the peak element found
    return list_of_integers[left]

