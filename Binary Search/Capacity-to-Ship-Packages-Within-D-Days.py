class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        a = max(weights)
        b = sum(weights)
        while a <= b:
            mid = (a + b)//2
            if self.capacity(mid, weights, days):
                b = mid - 1
            else:
                a = mid + 1
        return a

                

    def capacity(self, k: int, weights: List[int], days: int):
        count = 0
        a = 0 
        weight = 0
        while a < len(weights):
            if weight + weights[a] == k:
                count += 1
                a += 1
                weight = 0
            elif weight + weights[a] > k:
                count += 1
                weight = 0
            elif weight + weights[a] < k:
                weight += weights[a]
                a += 1
        if weight != 0:
            count += 1
        if count <= days:
            return True
        return False
