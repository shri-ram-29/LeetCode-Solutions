class Solution:
    def convertToTitle(self, colnumber: int) -> str:
        title = ""
        while colnumber > 0:
            rem = (colnumber - 1) % 26
            colnumber = (colnumber - 1) // 26
            title = chr(rem+65) + title
        return title