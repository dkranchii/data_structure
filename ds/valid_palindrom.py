class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initialize two pointers start and end
        start, end = 0, len(s) - 1
        # Step 2: Iterate while start is less than end
        while start <= end:
            # Step 3: Check if the character at position 'start' is not alphanumeric. If so, increase start
            if not s[start].isalnum():
                start += 1
                continue
            # Step 4: Check if the character at position 'end' is not alphanumeric. If so, decrease 'end' and continue
            if not s[end].isalnum():
                end -= 1
                continue
            # Step 5: Compare the lowercase representation of both start and end
            if s[start].lower() != s[end].lower():
                # if they are not equal, return False
                return False
            else:
                # if they are equal, increment start and decrement end
                start += 1
                end -= 1
        # after the entire string check, return True
        return True
