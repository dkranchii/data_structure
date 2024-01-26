class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      #create start and end pointer based on the lenth of given sorted array
        start, end = 0, len(numbers) -1
        #itirate to check the sum wrt target
        while start <= end:
            currSum = numbers[start] + numbers[end]
            #if currSum is greater than target then reduce the end pointer by one
            if currSum > target:
                end -= 1
            #if currSum is lower than target then increse the start pointer by one
            elif currSum < target:
                start += 1
            #return the start+1 and end+1
            else:
                return [start+ 1, end +1]
        return []
