def fib_series (first, second, num_terms):
    if num_terms == 0:
        print("Series Printed")
        return
    else:
        print(first)
        fib_series(second, first+second, num_terms-1)

fib_series(0, 1, 5)
