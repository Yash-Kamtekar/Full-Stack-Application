def maximumUniqueSubarray(nums):

        hmap = {}
        l = 0
        rsum = 0
        ans = 0

        for r in range(len(nums)):

            if nums[r] not in hmap:

                rsum += nums[r]
                hmap[nums[r]] = rsum

            else:

                rsum -= hmap[nums[r]] + nums[r]

            ans = max(ans, rsum)

        return ans

print(maximumUniqueSubarray([4,2,4,5,6]))