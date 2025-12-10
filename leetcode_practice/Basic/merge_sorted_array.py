def merge(nums1, m, nums2, n):
    i = m - 1                     # 1
    j = n - 1                     # 2
    k = m + n - 1                 # 3

    while i >= 0 and j >= 0:      # 4
        if nums1[i] > nums2[j]:   # 5
            nums1[k] = nums1[i]   # 6
            i -= 1                # 7
        else:
            nums1[k] = nums2[j]   # 8
            j -= 1                # 9
        
        k -= 1                    # 10

    # Copy remaining elements from nums2
    while j >= 0:                 # 11
        nums1[k] = nums2[j]       # 12
        j -= 1
        k -= 1
