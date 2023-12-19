# from https://www.youtube.com/watch?v=GUhWeJyHBCU
# time complexity O(n^2), Memory complexity O(1)


def select_sort_list(unsorted_list: list):
    number_of_comparisons = 0
    for unsorted_list_start_index in range(len(unsorted_list)):
        smallest_element_value = float("inf")
        smallest_element_index = None

        for index in range(unsorted_list_start_index, len(unsorted_list)):
            number_of_comparisons += 1
            if unsorted_list[index] < smallest_element_value:
                smallest_element_value = unsorted_list[index]
                smallest_element_index = index

        temp = unsorted_list[unsorted_list_start_index]
        unsorted_list[unsorted_list_start_index] = unsorted_list[smallest_element_index]
        unsorted_list[smallest_element_index] = temp

    print("number_of_comparisons: ", number_of_comparisons)
    sorted_list = unsorted_list
    return sorted_list


if __name__ == "__main__":
    ul = [9, 5, 1, 4, 7, 2, 3]
    print("unsorted list: ", ul)
    print("sorted list: ", select_sort_list(ul))
