import re

# Regular expressions can be used to find a specific pattern of characters in strings like telephone numbers, e-mails,
# URLs, etc. Let's say we have the following text, and we want to find all URLs in this text.

some_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, ' \
            'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ' \
            'Ut enim ad https://www.microsoft veniam, quis nostrud exercitation ullamco ' \
            'laboris nisi ut aliquip ex ea commodo consequat. https://www.google.com' \
            'Duis aute irure dolor in reprehenderit in voluptate velit ' \
            'esse cillum dolore eu fugiat nulla http://www.apple.uk. Excepteur sint occaecat '\
            'cupidatat non proident, sunt in culpa qui officia deserunt mollit ' \
            'anim id est laborum.'


def main():
    # First I declare my pattern. Let's say I figured out the following pattern. The pattern has been simplified for
    # clarity of example.
    my_pattern = r'https?:\/\/[a-z]+\.[a-z]+[.[a-z]+]*'

    # Some of the symbols used in regular expression patterns are:
    # h letter h literally
    # s? letter s 0 or 1 time
    # \/ a symbol /
    # a-z letter from a to z
    # \d any digit
    # [a-z]+ one or more letters
    # [a-z]* zero or more letters
    # For more info visit: https://regex101.com/

    # You have to import a module called re to use regular expressions. To find all occurrences of pattern in the text I
    # have to call a findall method. The method returns a following list.
    print("Founded strings that match your pattern are: ", re.findall(my_pattern, some_text))


if __name__ == '__main__':
    main()
