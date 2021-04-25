# def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
        # N = len(nums)
        # if N <= 1: return N
        # i = j = 1
        # while i < N:
        #     if nums[i] != nums[i-1]:
        #         nums[j] = nums[i]
        #         j +=1
        #     i +=1
        # return j
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     removeDuplicates([1,2,2,3,4,5,5,5])


class RemoveDuplicates:
    def removeDuplicates(self, nums):
        N = len(nums)
        if N <= 1: 
            return N
        i = j = 1
        while i < N:
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j +=1
            i +=1
        return j
test_Remove = RemoveDuplicates()
print(test_Remove.removeDuplicates([1,2,2,3,4,5,5,5]))


     

# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
