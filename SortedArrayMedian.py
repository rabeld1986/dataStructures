"""Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays."""
import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr_f = nums1 + nums2
        arr_f.sort()
        
        if len(arr_f) % 2 != 0:
            m = math.floor((len(arr_f)/2))
            med = arr_f[m]
            return med
        else:
            l = len(arr_f)
            m = int(l/2)
            p1 = arr_f[m-1]
            p2 = arr_f[m]
            
            med = (p1+p2) / 2
            return med
