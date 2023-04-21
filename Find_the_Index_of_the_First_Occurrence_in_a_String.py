class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_len = len(haystack)
        needle_len = len(needle)
        for i in range(haystack_len - needle_len + 1):
            j = 0
            while j < needle_len and haystack[i + j] == needle[j]:
                j += 1
            if j == needle_len:
                return i
        return -1