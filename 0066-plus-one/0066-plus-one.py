
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):

            if digits[i] < 9:
                digits[i] += 1
                return digits

            # If digit is 9, make it 0 and carry 1
            digits[i] = 0

        # If all digits were 9, add 1 at the beginning
        return [1] + digits
