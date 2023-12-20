# time complexity O(n^2) but if data is already sorted then O(n),
# Memory complexity O(1)

def insertion_sort_list(unsorted_list: list):
    for sorted_list_end_index in range(len(unsorted_list) - 1):
        temp = unsorted_list[sorted_list_end_index + 1]

        index = sorted_list_end_index
        while index >= 0 and unsorted_list[index] > temp:
            unsorted_list[index + 1] = unsorted_list[index]
            index -= 1

        unsorted_list[index + 1] = temp
    return unsorted_list


if __name__ == "__main__":
    ul = [2, 5, 1, 4, 7, 9, 3]
    print(ul)
    print(insertion_sort_list(ul))
