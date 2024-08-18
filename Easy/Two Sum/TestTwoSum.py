
from TwoSum import Solution

def test_twoSum():
    solution = Solution()

    # Test case 1: Example 1 from the problem statement
    nums = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    assert solution.twoSum(nums, target) == expected, f"Test case 1 failed"

    # Test case 2: Example 2 from the problem statement
    nums = [3, 2, 4]
    target = 6
    expected = [1, 2]
    assert solution.twoSum(nums, target) == expected, f"Test case 2 failed"

    # Test case 3: Example 3 from the problem statement
    nums = [3, 3]
    target = 6
    expected = [0, 1]
    assert solution.twoSum(nums, target) == expected, f"Test case 3 failed"

    # Test case 4: Single pair, first and last elements
    nums = [1, 5, 3, 7, 2]
    target = 3
    expected = [0, 4]
    assert solution.twoSum(nums, target) == expected, f"Test case 4 failed"

    # Test case 5: Negative numbers
    nums = [-3, 4, 3, 90]
    target = 0
    expected = [0, 2]
    assert solution.twoSum(nums, target) == expected, f"Test case 5 failed"

    # Test case 6: Large numbers
    nums = [230, 863, 916, 585, 981, 121, 866, 934, 857, 174]
    target = 1850
    expected = [2, 7]
    assert solution.twoSum(nums, target) == expected, f"Test case 6 failed"

    print("All test cases passed!")
    


# Run the test function
if __name__ == "__main__":
    test_twoSum()
