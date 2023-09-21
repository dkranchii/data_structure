class Solution:
    def binary_search(self, matrix, target, start, vertical):
        lo = start
        # set the length based on vertical or horiontal search
        hi = len(matrix[0]) - 1 if vertical else len(matrix) - 1

        #compare the target using binary search
        while hi >= lo:
            mid = (lo + hi ) // 2
            #searching the target in column
            if vertical:
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid -1
                else:
                    return True
            #searching in a row
            else:
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid -1
                else:
                    return True

        return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # an empty matrix 
        if not matrix:
            return False
        #iterate over matrix diagonals
        for i in range(min(len(matrix), len(matrix[0]))):
            vertical_found = self.binary_search(matrix, target, i, True)
            horizontal_found = self.binary_search(matrix, target, i , False )
            if vertical_found or horizontal_found:
                return True

        return False
        
