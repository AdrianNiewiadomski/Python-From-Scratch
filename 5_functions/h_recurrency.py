# Let's calculate Fibonacci sequence using recursion.
def fibonacci_1(n: int):
    if n == 0 or n == 1:
        return n
    else:
        # Recursion is the process a procedure goes through when one of the steps
        # of the procedure involves invoking the procedure itself.
        # Here it simplifies the process of obtaining the result of calculation.
        return fibonacci_1(n - 1) + fibonacci_1(n - 2)


# We may also perform calculations without it (recursion).
def fibonacci_2(n: int):
    values = [0, 1]

    if n > 1:
        for i in range(2, n + 1):
            values.append(values[i - 1] + values[i - 2])

    return values[n]


if __name__ == "__main__":
    # For small numbers, the method using recursion  works without problems.
    for k in range(11):
        print(k, ": ", fibonacci_1(k))

    # However for "greater" numbers a problem appears. As for 100 the calculations will take much longer.

    # k = 100
    # print(k, ": ", fibonacci_1(k))

    # This is because when we want to calculate the value of the function for n,
    # we must calculate the value for n - 1 and for n - 2. But to calculate value for n - 1
    # we must calculate the value for n - 2 and n - 3. This way we calculate fun(n -1) once,
    # fun(n - 2) twice, fun(n - 3) three times and so on.
    # Moreover, recursion uses the stack. So, to prevent stack overflow,
    # if the recursion exceeds a certain level, a following exception will be thrown:
    # "RecursionError: maximum recursion depth exceeded".

    print("And without recursion")

    # The second function stores calculated values in a list. Therefore, every value is calculated only once.
    for k in range(11):
        print(k, ": ", fibonacci_2(k))

    # And it works for greater number without any problems.
    k = 100
    print(k, ": ", fibonacci_2(k))
