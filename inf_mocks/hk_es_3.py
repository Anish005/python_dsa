'''
find the peak element in the array , 
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.
'''

import sys
sys.stdout = open('/Users/aniiiish/Documents/Projects/python_dsa/inf_mocks/output.txt', 'w')
sys.stdin = open('/Users/aniiiish/Documents/Projects/python_dsa/inf_mocks/input.txt','r')

def peak(nums):
    l , r = 0 , len(nums) - 1
    while l < r:
        m = (l + r) >> 1
        if nums[m - 1] <= nums[m] >= nums[m + 1]:
            return m
        elif nums[m] < nums[m + 1]:
            l = m + 1
        else:
            r = m 
    return l
    
def main():
    t = int(input())
    for _ in range(t):
        nums = list(map(int, input().split()))
        print(peak(nums))
      
if __name__ == '__main__':
    main()