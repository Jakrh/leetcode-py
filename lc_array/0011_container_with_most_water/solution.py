#!/usr/bin/env python3

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        current_area = 0
        result = 0

        while left < right:
            current_area = (right - left) * min(height[left], height[right])
            result = max(result, current_area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return result
