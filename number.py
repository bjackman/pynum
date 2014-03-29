class Number(object):
    # Construct a Number from a string
    @classmethod
    def from_string(_class, string):
        char_list = [c for c in string]
        order = Number.one
        acc = Number.zero

        while char_list:
            char = char_list.pop()
            acc += Number._char_to_number[char] * order
            order *= Number.ten

        return acc

    # Build a number that follows `pred`, whose string representationg is
    # `string`
    def __init__(self, pred, string=None):
        self._pred = pred
        self._pred._succ = self
        self._succ = None

        if string:
            self._string = string
        else:
            self._string = None
            
    # (This getter might come in handy if you implement negatives, I guess)
    @property
    def pred(self):
        return self._pred

    @property
    def succ(self):
        if not self._succ:
            self._succ = Number(self)

        return self._succ

    def __add__(self, other):
        if other.__class__ is Zero:
            return self
        else:
            return (self + other.pred).succ

    def __sub__(self, other):
        if other.__class__ is Zero:
            return self
        return self.pred - other.pred

    def __mul__(self, other):
        temp = Number.zero
        for _ in range(other):
            temp += self

        return temp

    def __eq__(self, other):
        return self is other or (self - other).__class__ is Zero
    def __gt__(self, other):
        return bool(self - other)
    def __ge__(self, other):
        return self == other or self > other

    def __div__(self, other):
        count = Number.zero
        temp  = self - other
        while temp is not None:
            temp -= other
            count += Number.one
        return count

    def __mod__(self, other):
        temp = self

        while temp - other is not None:
            temp -= other

        return temp

    def __nonzero__(self):
        return True

    # FOR DEBUGGING ONLY!
    def __int__(self):
        return int(self._pred) + 1

    def __str__(self):
        if self._string is not None:
            return self._string

        ten = Number.nine.succ
        temp = self
        string = ""
        while temp:
            string = (temp % ten)._string + string
            temp /= Number.ten

        return string

class Zero(Number):
    def __init__(self):
        self._pred = None
        self._succ = None
        self._string = "0"

    def __int__(self):
        return 0

    def __sub__(self, other):
        if other.__class__ is Zero:
            return self
        # Negative numbers not implemented yet
        return None

    def __nonzero__(self):
        return False

Number.zero = Zero()

Number.one   = Number(Number.zero,  "1")
Number.two   = Number(Number.one,   "2")
Number.three = Number(Number.two,   "3")
Number.four  = Number(Number.three, "4")
Number.five  = Number(Number.four,  "5")
Number.six   = Number(Number.five,  "6")
Number.seven = Number(Number.six,   "7")
Number.eight = Number(Number.seven, "8")
Number.nine  = Number(Number.eight, "9")

Number._char_to_number = {
    "0":  Number.zero,
    "1":  Number.one,
    "2":  Number.two,
    "3":  Number.three,
    "4":  Number.four,
    "5":  Number.five,
    "6":  Number.six,
    "7":  Number.seven,
    "8":  Number.eight,
    "9":  Number.nine
}

Number.ten = Number.nine.succ

if __name__ == "__main__":
    five = Number.five
    three = Number.three
    ten = Number.nine.succ
    twenty = ten + ten

    sums = [
        "five + three",
        "five - three",
        "three - five",
        "twenty / three",
        "twenty / five",
        "three / twenty",
        "twenty % three",        
        "three % five",
        "three % three",
        "three == three",
        "three == five",
        "three > five",
        "five > three",
        "three >= five",
        "three >= three",
        "five >= three",
        "three * five",
        "five * three",
        "twenty * three",
    ]

    for sum_string in sums:
        print("%s\t=\t%s" % (sum_string, eval(sum_string)))
