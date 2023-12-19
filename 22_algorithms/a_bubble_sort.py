# time complexity (n - 1)^2 -> O(n^2), Memory complexity O(1)

def bubble_sort_list(unsorted_list: list):
    for _ in range(len(unsorted_list)):
        for index in range(len(unsorted_list) - 1):
            if unsorted_list[index] > unsorted_list[index + 1]:
                temp = unsorted_list[index]
                unsorted_list[index] = unsorted_list[index+1]
                unsorted_list[index+1] = temp

        print(unsorted_list)


if __name__ == "__main__":
    ul = [9, 5, 1, 4, 7, 2, 3]
    print(ul)
    bubble_sort_list(ul)
