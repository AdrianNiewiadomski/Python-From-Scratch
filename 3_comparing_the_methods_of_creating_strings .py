import time


if __name__ == '__main__':
    old_string_formatting_start = time.time()
    for i in range(10000000):
        'string_%d' % i
    old_string_formatting_end = time.time()

    string_formatting_start = time.time()
    for i in range(10000000):
        'string_{}'.format(i)
    string_formatting_end = time.time()

    string_for_f_formatting_start = time.time()
    for i in range(10000000):
        f'string_{i}'
    string_for_f_formatting_end = time.time()

    print('time for old formatting: ', old_string_formatting_end - old_string_formatting_start)
    print('time for formatting: ', string_formatting_end - string_formatting_start)
    print('time for f string formatting: ', string_for_f_formatting_end - string_for_f_formatting_start)
