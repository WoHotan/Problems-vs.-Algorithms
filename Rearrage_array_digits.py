def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    first_num = second_num = 0
    quick_sort(input_list, 0, len(input_list) - 1)
    for index, value in enumerate(input_list):
        if index % 2 == 0:
            first_num = first_num * 10 + value
        else:
            second_num = second_num * 10 + value
    return [first_num, second_num]


def quick_sort(input_list, begin_index, end_index):
    """
    Sorted input_list via quick sort.
    """
    if end_index <= begin_index:
        return
    pivot_idx = sort_partition(input_list, begin_index, end_index)
    quick_sort(input_list, begin_index, pivot_idx - 1)
    quick_sort(input_list, pivot_idx + 1, end_index)

def sort_partition(input_list, begin_index, end_index):
    pivot_idx = end_index
    pivot_value = input_list[pivot_idx]
    left_index = begin_index
    while pivot_idx != left_index:
        item = input_list[left_index]
        if item > pivot_value:
            left_index += 1
            continue
        input_list[left_index] = input_list[pivot_idx - 1]
        input_list[pivot_idx - 1] = pivot_value
        input_list[pivot_idx] = item
        pivot_idx -= 1
    return pivot_idx



def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail", output, test_case[0])

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
test_case = [[], []]                        #test empty input
test_function(test_case)
test_case = [[1], [1]]                      #test one element list
test_function(test_case)