class Solution:

    def findKthLargest(self, nums, k):
        k = len(nums) - k

        l, r = 0, len(nums)-1

        while True:
            pivot = nums[r]
            p = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            nums[p], nums[r] = nums[r], nums[p]

            if p < k:
                l = p + 1
            elif p > k:
                r = p - 1
            else:
                return nums[p]