class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        a = 0
        b = len(arr) - 1

        while a <= b:
            mid = (a + b)//2
            if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
                return mid
            elif arr[mid] > arr[mid + 1]:
                b = mid
            else:
                a = mid + 1
