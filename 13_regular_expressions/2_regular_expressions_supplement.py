import re
# Let's say that we want to check if a searched pattern (a telephone number) is in a given text.

some_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, ' \
            'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ' \
            'Ut enim ad veniam, quis nostrud exercitation ullamco ' \
            'laboris nisi ut aliquip  1-888-280-4331 ex ea commodo consequat. ' \
            'Duis aute irure dolor in 1 888 280 4331 reprehenderit in voluptate velit ' \
            'esse cillum dolore eu fu 18882804331 giat nulla. Excepteur sint occaecat '\
            'cupidatat non proident, sunt in culpa qui officia deserunt mollit ' \
            'anim id est laborum.'

print("some_text: ", some_text)

# We choose the following formula for a telephone number.
pattern = r"\d+([ -]?[\d]*)*"

# To find out whether our pattern is in the analyzed text we can use the search method.
result = re.search(pattern, some_text)  # This is None if the pattern is not in the text.

# Therefore, we may use the if clause. Notice that printed results concern only the first occurrence of pattern in the
# text. All results can be received with re.findall or re.finditer.
if result:
    print(result.group())
    print(result.start())
    print(result.end())

# The example of re.finditer has been shown below.
results = re.finditer(pattern, some_text)
for result in results:
    print(result)
    print(result.group())

# To apply the pattern at the start of the string you can use re.match. This is useful if the string should start with
# the pattern. Similarly, if the whole string should fit the pattern use re.fullmatch.
match = re.match(pattern, "1 888 280 4331 rest of the text.")
print(match.group())

match = re.match(pattern, "a 1 888 280 4331 rest of the text.")
# If the pattern has not been found, the attempt to call a method of the result of searching will couse AttributeError.
# print(match.group())  # AttributeError: 'NoneType' object has no attribute 'group'
