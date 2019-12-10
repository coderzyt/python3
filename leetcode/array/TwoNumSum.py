class TwoNumSum(object):
    
    # 暴力解法
    def two_num_sum1(self, nums: list, target: int) -> list:
        if nums.__len__() < 2:
            return []
        for i in range(0, nums.__len__()):
            for j in range(i+1, nums.__len__()):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
    # 哈希
    def two_num_sum2(self, nums: list, target: int) -> list:
        if nums.__len__() < 2:
            return []
        map = {}
        for index, num in enumerate(nums):
            another = target - num
            if another in map:
                return [map[another], index]
            map[num] = index
        return []

    def two_num_sum3(self, nums: list, target: int) -> list:
        if nums.__len__() < 2:
            return []
        hashmap = dict()
        for i in range (0, nums.__len__()):
            another = target - nums[i]
            if hashmap.__contains__(another):
                return [hashmap.__getitem__(another), i]
            hashmap.__setitem__(nums[i], i)
        return []
                
if __name__ == "__main__":
    nums = [0, 1, 2, 3, 4, 5, 6, 7]
    target = 13
    twoNumSum = TwoNumSum()
    result = twoNumSum.two_num_sum3(nums, target)
    print(result)