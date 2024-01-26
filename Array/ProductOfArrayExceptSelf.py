#Solution to https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        #make an array of 1s
        product = [1] * length
        prefix = 1
        postfix = 1

        for i in range(length):
            #multiply current position by its prefix
            product[i] *= prefix
            #move prefix forward by multiplying it with the current element
            prefix *= nums[i]
            #define the other end of the products array by multiplying it with postfix. This will eventually reach the current position so that the product becomes the multiplication of prefix and postfix.
            product[length - i - 1] *= postfix
            #move postfix forward by similary multiplying it with the next element on the right
            postfix *= nums[length - i - 1]

        #product array is now the product of the prefix and postfix for every element in the original array
        return product