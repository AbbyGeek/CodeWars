def remove_smallest(numbers):
    if numbers == []: return numbers
    numbers.remove(min(numbers))
    return numbers