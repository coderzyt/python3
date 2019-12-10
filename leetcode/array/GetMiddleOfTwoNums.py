class GetMiddleOfTwoNums(object):

    def getMiddleOfTwoNums(self, nums1: list, nums2: list) -> int:
        length1 = nums1.__len__()
        length2 = nums2.__len__()
        if length1 < 1:
            return self.getMiddle(nums2)
        if length2 < 1:
            return self.getMiddle(nums1)
        
        nums = list()
        i, j, k = 0, 0, 0
        while k < length1 + length2:
            if i > length1 - 1:
                nums.append(nums2[j])
                j = j + 1
            elif j > length2 - 1:
                nums.append(nums1[i])
                i = i + 1
            else:
                if nums1[i] <= nums2[j]:
                    nums.append(nums1[i])
                    i = i + 1
                elif nums2[j] <= nums1[i]:
                    nums.append(nums2[j])
                    j = j + 1
            k = k + 1
        return self.getMiddle(nums)
    
    def getMiddle(self, nums: list) -> float:
        length = nums.__len__()
        if length % 2 == 0:
            result = (nums[int(length / 2)] + nums[int((length - 2) / 2)]) / 2
        else:
            result = nums[int((length - 1) / 2)]
        return result

if __name__ == "__main__":
    # nums1 = [0, 1, 2, 4, 5]
    # nums2 = [3]
    nums1 = [0, 0]
    nums2 = [0, 0]
    getMiddleOfTwo = GetMiddleOfTwoNums()
    print(getMiddleOfTwo.getMiddleOfTwoNums(nums1, nums2))