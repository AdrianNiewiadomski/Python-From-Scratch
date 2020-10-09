def my_divide_function(a, b):
    return a / b


def main():
    print('In this example it will be demonstrated what are exceptions and how to deal with them.')
    print('In the script above there is a simple function that performs an operation of division.')
    print('The function usually works fine. For instance')
    print('my_divide_function(1, 2) = ', my_divide_function(1, 2))

    print('\nHowever, calling the function with second argument equal to 0'
          ' (my_divide_function(1, 0)) will raise a ZeroDivisionError.')

    print('\nTherefore it is recommended to enclose a potentially dangerous code in a try-except block.')
    try:
        my_divide_function(1, 0)
    except ZeroDivisionError:
        print('Thou Shalt Not Divide by Zero! ;)')


if __name__ == '__main__':
    main()