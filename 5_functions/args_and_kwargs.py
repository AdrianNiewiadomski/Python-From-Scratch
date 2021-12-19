# Using *arg is a convenient way to enable user to pass a variable number of the arguments to function.
def concatenate(*args, prefix='', connector=''):
    result = prefix
    for arg in args:
        result += str(arg) + connector

    return result


# You may also use **kwargs to pass variable number of keyword arguments
def create_query(**kwargs):
    what = ', '.join(kwargs['what'])
    return 'SELECT {} FROM {}'.format(what, kwargs['from_where'])


def main():
    print(concatenate('Mary', 'had', 'a', 'little', 'lamb', connector=' '))
    print(concatenate('home', 'adrian', 'documents', prefix='/', connector='/'))
    print(concatenate('github.com', 'AdrianNiewiadomski', 'Python-From-Scratch',
                      prefix='https://', connector='/'))
    print(concatenate('jenkins46', 9346, '14ju73', 'Mary', 'Jenkins', 'Engineering', 'Manchester', connector=';'), '\n')

    print(create_query(what=['name', 'age', 'email'], from_where='users'))


if __name__ == '__main__':
    main()
