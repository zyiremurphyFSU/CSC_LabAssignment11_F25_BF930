def sum_list(numbers):
    """
    Calculate the sum of all numbers in a list.

    @param numbers (list of int): List of integer numbers.

    @return int: Sum of the list elements.
    """

    total = 0
      
    for num in numbers:
        total += num

    return total


if __name__ == "__main__":
    nums = [5, 19, 2, 33, -5, 2]
    print(sum_list(nums))
