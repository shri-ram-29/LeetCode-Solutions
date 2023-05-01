from typing import List
class Solution:
    def PlusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits),-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits.insert(0,1)
        return digits