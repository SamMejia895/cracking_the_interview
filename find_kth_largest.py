import heapq

def find_kth_largest(nums: list[int], k: int) -> int:
    """
    Finds the k-th largest element in an array using a Min-Heap.
    """
    # 1. Initialize a Min-Heap (priority queue)
    min_heap = []

    # 2. Iterate through all elements in the array
    for num in nums:
        # Add the current number to the heap
        heapq.heappush(min_heap, num)
        
        # 3. Maintain the heap size to be exactly k
        # If the heap size exceeds k, the smallest element in the heap 
        # (which is the root) is not among the k largest elements overall, 
        # so we pop it.
        if len(min_heap) > k:
            heapq.heappop(min_heap)
            
    # 4. The k-th largest element is the smallest element currently in the heap
    # (i.e., the root of the Min-Heap)
    return min_heap[0]

# --- Examples ---

# Example 1:
nums1 = [3, 2, 1, 5, 6, 4]
k1 = 2
result1 = find_kth_largest(nums1, k1)
print(f"Input: {nums1}, k={k1}")
print(f"Output: {result1} (Correct: 5)")
# The heap ends up as [5, 6], smallest is 5

# Example 2:
nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k2 = 4
result2 = find_kth_largest(nums2, k2)
print(f"Input: {nums2}, k={k2}")
print(f"Output: {result2} (Correct: 4)")
# The heap ends up containing the 4 largest: [4, 5, 5, 6], smallest is 4
