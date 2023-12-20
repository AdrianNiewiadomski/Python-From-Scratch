comparisons = 0


def merge_list(list_1, list_2):
    sorted_list = []

    i = 0
    j = 0

    for _ in range(len(list_1) + len(list_2)):
        if i >= len(list_1) or j >= len(list_2):
            break

        if list_1[i] < list_2[j]:
            sorted_list.append(list_1[i])
            i += 1
        else:
            sorted_list.append(list_2[j])
            j += 1
        global comparisons
        comparisons += 1

    for el in sorted_list:
        if el in list_1:
            list_1.remove(el)
        if el in list_2:
            list_2.remove(el)

    sorted_list = sorted_list + list_1
    sorted_list = sorted_list + list_2
    return sorted_list


def merge_sort_list(unsorted_list: list):

    if len(unsorted_list) == 1:
        return unsorted_list

    if len(unsorted_list) > 1:
        ul1 = unsorted_list[:len(unsorted_list) // 2]
        ul2 = unsorted_list[len(unsorted_list) // 2:]
        return merge_list(
            merge_sort_list(ul1),
            merge_sort_list(ul2)
        )


if __name__ == "__main__":
    ul = [2, 5, 1, 4, 7, 9, 3]
    print(ul)
    print(merge_sort_list(ul))
    print("Total comparisons: ", comparisons)
