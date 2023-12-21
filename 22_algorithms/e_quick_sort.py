comparisons = 0


def quick_sort_list(unsorted_list: list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    border = 0
    pivot = unsorted_list[-1]
    global comparisons

    for index in range(len(unsorted_list) - 1):
        element = unsorted_list[index]
        if element < pivot and border == index:
            border += 1

        elif element < pivot:
            temp = unsorted_list[border]
            unsorted_list[border] = unsorted_list[index]
            unsorted_list[index] = temp
            border += 1

        comparisons += 1

    temp = unsorted_list[border]
    unsorted_list[border] = unsorted_list[-1]
    unsorted_list[-1] = temp

    result = quick_sort_list(unsorted_list[:border]) + [unsorted_list[border]] + quick_sort_list(unsorted_list[border + 1:])
    return result


if __name__ == "__main__":
    ul = [2, 5, 1, 4, 7, 9, 3]
    print(ul)
    print(quick_sort_list(ul.copy()))
    print("Total comparisons: ", comparisons)
