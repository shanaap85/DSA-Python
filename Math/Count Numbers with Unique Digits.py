class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        Dict = {0: 1,
        1 : 9,
        2 : 9*9,
        3 : 9*9*8,
        4 : 9*9*8*7,
        5 : 9*9*8*7*6,
        6 : 9*9*8*7*6*5,
        7 : 9*9*8*7*6*5*4,
        8 : 9*9*8*7*6*5*4*3}

        Pro = 0
        for i in range(n+1):
            Pro += Dict[i]

        return Pro
