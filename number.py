"""
An implementation of positive integer arithmetic. I was thinking about this late
at night and decided the easiest way to stop it keeping me awake on subsequent
nights would be to just implement it. It was quite fun getting to know the 
Python data model a bit better.

I made sure not to think about performance (that's boring). There are also
plenty of fun things that could be added:
    - Some of the other __*__ stuff is missing. See:
      http://docs.python.org/2/reference/datamodel.html
    - Negative numbers - there are a couple of different ways to implement this.
    - I don't really know the maths but I think imaginary numbers might be quite
      easy too, and maybe even complex?
    - Bitwise operators
    - Real numbers (?)
    - addition > multiplication > exponentiation is a series. It would be nice
      to just define __add__ and have __mul__ and __pow__ and <whatever you call
      the "next" operation> inductively defined! I think you could do the same
      for __div__ but now my head hurts (does the series actually go 
        division-by-power < division < subtraction < addition > multiplication)?
    - Hack Python to get it to let you pass an arbitrary object as a list index!
"""
class Number(object):
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
        return (self.pred * other) + other

    def __pow__(self, other):
        if other.__class__ is Zero:
            return other.succ
        return (self ** other.pred) * self

    def __eq__(self, other):
        return self is other or (self - other).__class__ is Zero
    def __ne__(self, other):
        return self is not other and (self - other).__class__ is not Zero
    def __gt__(self, other):
        return bool(self - other)
    def __ge__(self, other):
        return self == other or bool(self - other)
    def __lt__(self, other):
        return bool(other - self)
    def __le__(self, other):
        return self == other or bool(other - self)

    def __div__(self, other):
        count = Number.zero
        temp  = self - other
        while temp is not None:
            temp -= other
            count = count.succ
        return count

    def __mod__(self, other):
        temp = self

        while temp - other is not None:
            temp -= other

        return temp

    def __nonzero__(self):
        return True

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

    def __sub__(self, other):
        if other.__class__ is Zero:
            return self
        # Negative numbers not implemented yet
        return None

    def __mul__(self, other):
        return self

    def __nonzero__(self):
        return False

# For bootstrapping the conversion to strings:

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

# Just for convenience:
Number.ten = Number.nine.succ