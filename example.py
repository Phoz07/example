def find_single_occurrence_numbers(numbers: list) -> list:
    '''Main function'''
    num_lst = []
    for number in numbers:
        if numbers.count(number) == 1:
            num_lst.append(number)
    return num_lst
print(find_single_occurrence_numbers([4, 5, 6, 4, 7, 5, 8]))
print(find_single_occurrence_numbers([1, 2, 2, 3, 3, 4, 4]))
