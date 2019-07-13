  Because the rotated array is sorted, so just find the rotat index, divide the array into two ordered parts. First, determine which side the target falls on, and then apply binary search to find the target index.

  The time complexity of find_min_number_index function is O(log(n)), and the time complexity of binary search function also O(log(n)), which n is the length of the array. The space complexity is O(1)
