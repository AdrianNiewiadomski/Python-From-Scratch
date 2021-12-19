import re

some_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, ' \
            'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ' \
            'Ut enim ad https://www.microsoft veniam, quis nostrud exercitation ullamco ' \
            'laboris nisi ut aliquip ex ea commodo consequat. https://www.google.com' \
            'Duis aute irure dolor in reprehenderit in voluptate velit ' \
            'esse cillum dolore eu fugiat nulla https://www.apple.uk. Excepteur sint occaecat '\
            'cupidatat non proident, sunt in culpa qui officia deserunt mollit ' \
            'anim id est laborum.'

def main():
    print('Let\'s say that I have a large amount of data to check.')
    print('I need to find all urls in some text.')
    print('I may use regular expressions to do that.')

    print('\nFirst I declare my pattern. Lets say I figured out a following pattern:')
    my_pattern = r'https?:\/\/[a-z]+\.[a-z]+[.[a-z]+]*'
    print(my_pattern)

    print('\nThe pattern has been simplified for clarity of example.')

    print('\nNow I have to import a module called re.')
    print('Then to find all occurrences of pattern in the text I have to call a findall method.')
    print('The method returns a following list')
    print(re.findall(my_pattern, some_text))


if __name__ == '__main__':
    main()
