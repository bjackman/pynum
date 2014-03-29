"""
I guess if I'm going to share this I should probably test it..

We don't test behaviour of "invalid" stuff like a - b where b > a (negative 
numbers aren't implemented), or division by zero. 
We also assume the conversions to and from strings are OK.
"""

from number import Number, Zero

if __name__ == "__main__":
    sums = [
        "1 + 1",
        "5 + 3", 
        "3 + 3", 
        "3 + 6", 
        "4 + 0",
        "0 + 4",

        "7 - 0",
        "5 - 3",
        "1 - 1",
        "15 - 15",
        "6 - 2",

        "0 * 10",
        "0 * 0",
        "10 * 0",
        "12 * 1",
        "1 * 13",
        "13 * 4",

        "3 == 3",
        "3 == 5",
        "6 == 2",
        "0 == 0",
        "1 == 0",
        "0 == 1",

        "3 != 3",
        "3 != 5",
        "6 != 2",
        "0 != 0",
        "1 != 0",
        "0 != 1",

        "0 > 8",
        "0 > 0",
        "11 > 0",
        "2 > 7",
        "3 > 3",
        "6 > 2",

        "0 >= 8",
        "0 >= 0",
        "11 >= 0",
        "2 >= 7",
        "3 >= 3",
        "6 >= 2",

        "0 < 8",
        "0 < 0",
        "11 < 0",
        "2 < 7",
        "3 < 3",
        "6 < 2",

        "0 <= 8",
        "0 <= 0",
        "11 <= 0",
        "2 <= 7",
        "3 <= 3",
        "6 <= 2",
        
        "20 / 3",
        "20 / 5",
        "3 / 20",
        "3 / 21",
        "0 / 9",

        "20 % 3",        
        "3 % 5",
        "3 % 3",
        "0 % 4",

        "0 ** 0",
        "0 ** 3",
        "5 ** 0",
        "2 ** 2",
        "5 ** 3",
        "3 ** 5",
    ]

    for sum_string in sums:

        try:
            eval_string = 'Number.from_string("%s") %s Number.from_string("%s")' \
                          % tuple(sum_string.split())

            result = str(eval(eval_string))

            python_result = str(eval(sum_string))

            assert(result == python_result)
        except AssertionError:
            print("Failure: %s = %s" % (sum_string, result))
        except:
            print("Crash evaluating '%s'\n" % eval_string)
            raise
