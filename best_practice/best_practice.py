

def larger_or_difference_number(first_num, second_num):
    """
    Adds up any amount of numbers I give it. It starts at 0, goes through each number, and returns the total. Super simple on purpose so it’s easy to read.
    """
    
    #validation
    if not isinstance(first_num, (int, float)) or not isinstance(second_num, (int, float)):
        return "Error: please pass numbers (int or float)."

    #zero case
    if first_num == 0 or second_num == 0:
        return "Zero found"

    #both positive: print larger 'smaller' times
    if first_num > 0 and second_num > 0:
        larger = first_num if first_num > second_num else second_num
        smaller = first_num if first_num < second_num else second_num

        # range() needs an int; if someone passes a float, the int part can be used.
        times = int(smaller)
        for _ in range(times):
            print(larger)
        return  # printed only; nothing to return

    #otherwise (negatives or mixed signs): to keep thi original behavior
    if first_num < second_num:
        return first_num - second_num
    return second_num - first_num


if __name__ == "__main__":
    # both positive: prints 5 three times
    larger_or_difference_number(5, 3)

    # zero case
    print(larger_or_difference_number(0, 7))  # will return "Zero found"

    # negatives/mixed signs
    print(larger_or_difference_number(-2, 5))  # will return -7
    print(larger_or_difference_number(2, -5))  # will return -7

    # non-numeric input 
    print(larger_or_difference_number("5", 3))  # this will give the following "Error: please pass numbers .. int or float."
