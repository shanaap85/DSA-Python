class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        summ = 1
        i = 2
        if num == 1:
            return False
        while i*i <= num:
            if num % i == 0 and i != num//i:
                summ += i
                summ += num//i
            elif num % i == 0 and num//i == i:
                summ += i
            i += 1
        if summ == num:
            return True
        return False
