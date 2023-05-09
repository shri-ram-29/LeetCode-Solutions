from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq = {}
        for c in p:
            freq[c] = freq.get(c,0)+1
        counter = len(p)
        start = 0; end = 0; result = []
        while end < len(s):
            if s[end] in freq:
                if freq[s[end]] > 0:
                    counter -= 1
                freq[s[end]] -= 1
            end += 1
            
            if counter == 0:
                result.append(start)
            if end - start == len(p):
                if s[start] in freq:
                    if freq[s[start]] >= 0:
                        counter += 1
                    freq[s[start]] += 1
                start += 1
        return result