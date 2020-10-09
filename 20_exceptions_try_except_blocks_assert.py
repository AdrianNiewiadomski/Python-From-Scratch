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

    print('\nSometimes you want to raise an exception.')
    print('For instance to warn a fellow programmer about incorrect usage of your module.')
    print('Other case may be to make sure that some requirements are met before further run of program.')
    print('You may also use exceptions during a debug process.')
    config = {
        'a': 1,
        'b': 2,
        # 'host_ip': '127.0.0.1'
    }
    print('\nLets say some other module provided a config: ', config)
    print('To make sure a required field \'host_ip\' is present in config use an assert keword.')
    print('A lack of \'host_ip\' will result in following exception: ')
    assert 'host_ip' in config, 'You must provide a host ip in the config!'


if __name__ == '__main__':
    main()
