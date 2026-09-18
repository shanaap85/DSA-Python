class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        L = []
        a = len(num) - 1
        carry = 0

        while a >= 0 or k > 0 or carry:
            digit = num[a] if a >= 0 else 0

            ans = digit + (k % 10) + carry
            carry = ans // 10

            L.append(ans % 10)

            k //= 10
            a -= 1

        return L[::-1]
