#
# author    Raul Aguilar
# date      July 16, 2020
#
# CS 138 1535 Homework 13 Project 1
# Compare the sort times of python standard sort, selection sort and
# merge sort for the list sizes of 5000, 50000, and 500000
#
# Algorithm:
# 1. Open text file containing numbers
# 2. Read numbers into a list
# 3. Sort the list
# 4. Print results to text file
#


def selSort(nums):
    """Sort nums into ascending order."""
    n = len(nums)

    # For each position in the list (except the very last)
    for bottom in range(n-1):
        # find the smallest item in nums[bottom]..nums[n-1]
        mp = bottom                     # bottom is smallest initially
        for i in range(bottom+1, n):    # look at each position
            if nums[i] < nums[mp]:      # this one is smaller
                mp = i                  # remember its index

        # swap smallest item to the bottom
        nums[bottom], nums[mp] = nums[mp], nums[bottom]


def merge(lst1, lst2, lst3):
    """Merge sorted lists list1 and list2 into list3"""

    # These indexes keep track of current position in each list
    i1, i2, i3 = 0, 0, 0                # all start at the front
    n1, n2 = len(lst1), len(lst2)

    # Loop while both list1 and list2 have more items
    while i1 < n1 and i2 < n2:
        if lst1[i1] < lst2[i2]:
            lst3[i3] = lst1[i1]
            i1 += 1
        else:
            lst3[i3] = lst2[i2]
            i2 += 1
        i3 += 1

    # Here either list1 or list2 is done. One of the following loops
    # will execute to finish up the merge
    
    # Copy remaining items (if any) from last
    while i1 < n1:
        lst3[i3] = lst1[i1]
        i1 += 1
        i3 += 1
    
    # Copy remaining items (if any) from list2
    while i2 < n2:
        lst3[i3] = lst2[i2]
        i2 += 1
        i3 += 1

    
def mergeSort(nums):
    # Put items of nums in ascending order
    n = len(nums)

    # Do nothing if nums contains 0 or 1 items
    if n > 1:
        # Split into two sublists
        m = n//2
        nums1, nums2 = nums[:m], nums[m:]

        # Recursively sort each piece
        mergeSort(nums1)
        mergeSort(nums2)

        # Merge the sorted pieces back into original list
        merge(nums1, nums2, nums)


def main():
    filename = "numbers.txt"
    infile = open(filename, "r")
    nums = []

    for line in infile:
        nums.append(int(line))

    infile.close()
    outfile = open("hw13project1.txt", "w")

    print(nums, file=outfile)
    mergeSort(nums)
    print(nums, file=outfile)


main()
