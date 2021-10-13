"""Summarize data values to support data analysis."""

from typing import List

# correct all of the needed type annotations


def compute_mean(numbers: List[float]) -> float:
    """Compute the mean of a list of numbers."""
    # Refer to the book called "Doing Math with Python"
    # for details about how to implement this function
    # sum the list of the numbers
    sum_of_num = sum(numbers)
    # determine the length of the list of numbers
    len_of_num = len(numbers)
    # as long as the computation will not be an
    # undefined division by zero, compute the mean
    # https://stackoverflow.com/questions/58400652/average-returning-a-value-even-when-list-is-empty
    # if the list was empty, then return a mean that is "not a number"
    # https://stackoverflow.com/questions/944700/how-can-i-check-for-nan-values
    if numbers:
        return sum_of_num / len_of_num
    else:
        return float("nan")


def compute_median(numbers: List[float]) -> float:
    """Compute the median of a list of numbers."""
    # Refer to the book called "Doing Math with Python"
    # for details about how to implement this function
    # as long as the computation will not be an
    # undefined division by zero, compute the median
    if numbers:
        numbers.sort()
        len_of_num = len(numbers)
        # sort the numbers in an "in place" fashion
        if len_of_num % 2 == 0:
            mid1 = int(len_of_num / 2)
            mid2 = mid1 - 1
            med = compute_mean([numbers[mid1], numbers[mid2]])
            return med
        else:
            m = (len_of_num + 1) / 2
            m = int(m) - 1
            med = numbers[m]
            return med
        # case: the count of the values is even
        # get the two indices that are before and after the middle
        # convert to an integer to prepare for indexing
        # adjust for the fact that lists index starting at 0
        # compute the median value
        # case: the count of the values is odd
        # convert to an integer to prepare for indexing
        # adjust for the fact that lists index starting at 0
    # if the list was empty, then return a median that is "not a number"
    # return the computed median value
    else:
        return float("NaN")


def compute_difference(numbers: List[float]) -> List[float]:
    """Compute difference for each value from the calculated mean."""
    # Refer to the book called "Doing Math with Python"
    # for details about how to implement this function
    # compute the mean
    m = compute_mean(numbers)
    # compute the differences from the mean
    diff = []
    for num in numbers:
        diff.append(num - m)
    # return the computed differences from the mean
    return diff


def compute_variance(numbers: List[float]) -> float:
    """Compute the variance of a list of numbers."""
    # compute the difference from the mean
    diff = compute_difference(numbers)
    # compute the squared differences
    squared_diff = []
    for d in diff:
        squared_diff.append(d ** 2)
    # calculate the variance
    sum_sqaured_diff = sum(squared_diff)
    variance = sum_sqaured_diff / len(numbers)
    # return the calculated variance of the list of numbers
    return variance


def compute_standard_deviation(numbers: List[float]) -> float:
    """Compute the standard deviation of a list of numbers."""
    # call the function to calculate the variance
    variance = compute_variance(numbers)
    # calculate the standard deviation as the square root of the variance
    std = variance ** 0.5
    # return the calculated standard devision of the list of numbers
    return std
