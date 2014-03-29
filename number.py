class Number(object):
    @classmethod
    def from_python_int(self, python_int):
        if python_int == 0:
            return Number.zero

        return Number.from_python_int(python_int - 1).succ

    def __init__(self, pred, string=None):
        self._pred = pred
        self._pred._succ = self
        self._succ = None

        if string:
            self._string = string
        else:
            self._string = None
            
    # TODO necessary?
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

    def __eq__(self, other):
        return self is other or (self - other).__class__ is Zero
    def __gt__(self, other):
        return bool(self - other)
    def __ge__(self, other):
        return self == other or self > other

    def __div__(self, other):
        count = Number.zero
        temp = self
        while temp:
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
            temp /= ten

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

if __name__ == "__main__":
    five = Number.five
    three = Number.three
    twenty = Number.from_python_int(20)

    sums = [
        "five + three",
        "five - three",
        "three - five",
        "twenty / three",
        "twenty / five",
        "twenty % three",        
        "three % five",
        "three % three",
        "three == three",
        "three == five",
        "three > five",
        "five > three",
        "three >= five",
        "three >= three",
        "five >= three"

    ]

    for sum_string in sums:
        print("%s\t=\t%s" % (sum_string, str(eval(sum_string))))
