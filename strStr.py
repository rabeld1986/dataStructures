"""Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack."""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)
        if len(needle) == 0:
            return 0
        if needle not in haystack:
            return -1
        else:
            for i in range(len(haystack)):
                
                sub = haystack[i:l]
                if sub == needle:
                    return i
                l+=1
