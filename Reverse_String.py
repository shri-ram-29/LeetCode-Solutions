from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        pointer_one = 0; pointer_two = len(s) - 1
        for i in range(len(s) // 2):
            s[pointer_one], s[pointer_two] = s[pointer_two], s[pointer_one]
            pointer_one += 1; pointer_two -= 1
