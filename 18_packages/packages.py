# We will put groups of modules in packages.
# A directory that contains a file with a name __init__.py is considered package by Python
# The __init__.py file may be empty.
# U may use PyCharm, to automatically add __init__.py to your package.

# Two packages i.e. my_package and my_sub_package have been added to parent directory of this file.
import my_package.some_main_script


def main_1():
    # Now we can call functions from some_main_script
    my_string = my_package.some_main_script.concatenate("Mary", "had a little lamb")
    print(my_string)

    # If you opened the Pyhon-From-Scratch project in the PyCharm, the some_main_script is highlighted.
    # This is because of incorrect naming convention of the 18_packages directory.
    # Open 18_packages directly if you want PyCharm to stop highlight some_main_script
    # and to start give you hints about the package.

    # Now you may import a fun function from some_sub_script
    from my_package.my_sub_package.some_sub_script import fun as my_function
    my_function()

    # However the other function, namely fun2 is not imported and thus
    # an attempt to call it:
    # fun2()
    # will raise:
    # NameError: name 'fun2' is not defined


# To import all functions from a module use an asterisk operator
from my_package.my_sub_package.some_sub_script import *
# The use of asterisk operator is only allowed at module level
# Therefore it cannot be used in the body of function


def main_2():
    # Therefore an asterisk operator cannot be used in the body of function
    # from my_package.my_sub_package.some_sub_script import *
    # You may now use both functions from some_sub_script
    fun()
    fun2()

    # fun2 may also be called in following manner. Event without importing *
    my_package.my_sub_package.some_sub_script.fun2()


if __name__ == '__main__':
    main_1()
    main_2()
