def main():
    print('Files may be opened with a built in function open.')
    print('The function has two mandatory arguments. The path to file and a mode.')
    print('Some of these modes are r, a and w. These correspond to read, append and write.')

    file = open('data/king_lear.txt', 'r')
    print('After opening a file you may read it with the read method.')
    print('The method will return whole contains of a file. You may print the result:\n')
    print(file.read())
    print('\nor save it for further process.')
    print('After you have finished working with the file you should close it with method close.')
    file.close()

    print('\nMore convenient way of working with files is to open them in the with block.')
    print('This ensures that the file will be closed after the code in the with block has been executed.')
    with open('data/king_lear.txt', 'r') as file:

        print('You may read a file line by line simply by looping through it:\n')
        for line in file:
            print('\x1B[3m', line.replace('\n', ''), '\x1B[23m')


if __name__ == '__main__':
    main()
