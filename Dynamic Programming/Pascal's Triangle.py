class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        L = []

        for i in range(numRows):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = L[i - 1][j - 1] + L[i - 1][j]

            L.append(row)

        return L
