import heapq


def find_kth_largest(nums: list[int], k: int) -> int:

    heap = [-num for num in nums]

    print("before", heap)

    heapq.heapify(heap)

    print("after", heap)

    for i in range(k):

        number = heapq.heappop(heap)

        if i + 1 == k:

            return -number


nums1 = [3,2,1,5,6,4]

k1 = 2

result1 = find_kth_largest(nums1, k1)

print(f"input {nums1}, k:{k1}")

print(f"output {result1}")


nums2 = [3,2,4,1,2,4,5,5,6]

k2 = 4

result2 = find_kth_largest(nums2, k2)

print(f"input {nums2}, k:{k2}")

print(f"output {result2}")

