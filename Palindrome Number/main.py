from collections import deque

class Solution:
    def isPalindrome(self, x: int) -> bool:
        queue = deque([])
        for element in str(x):
            queue.append(element)

        while len(queue) > 1:
            last_item = queue.pop()
            first_item = queue.popleft()

            if first_item != last_item:
                return False

        return True