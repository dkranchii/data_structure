class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize result list with zeros, length equals to input array
        res = [0] * len(temperatures)
        # Stack to keep track of temperatures and their indices
        stack = []  # Stack format: [temperature, index]

        for i, t in enumerate(temperatures):
            # Iterate through each temperature and its index
            # Check if the stack is not empty and the current temperature is greater than the temperature at the top of the stack
            while stack and t > stack[-1][0]:
                # If yes, pop the temperature and index from the stack
                stack_tmp, stack_ind = stack.pop()
                # Calculate the difference between the current index and the index popped from the stack
                res[stack_ind] = (i - stack_ind)
            # Append the current temperature and its index to the stack
            stack.append([t, i])

        return res
