class Number(object):
    @classmethod
    def from_python_int(self, python_int):
        if python_int == 0:
            return Zero()

        return Number.from_python_int(python_int - 1).succ

    def __init__(self, pred, string=None):
        self._pred = pred
        self._succ = None

        # if string:
        #     self._string = string
        # else:
            
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

    def __div__(self, other):
        count = Zero()
        dec = self
        while dec:
            dec -= other
            count += Zero().succ
        return count

    def __nonzero__(self):
        return True

    # FOR DEBUGGING ONLY!
    def __int__(self):
        return int(self._pred) + 1

    def __str__(self):
        return self._string



class Zero(Number):
    def __init__(self):
        self._pred = None
        self._succ = None

    def __int__(self):
        return 0

    def __sub__(self, other):
        if other.__class__ is Zero:
            return self
        # Negative numbers not implemented yet
        return None

    def __nonzero__(self):
        return False


if __name__ == "__main__":
    five = Number.from_python_int(5)
    three = Number.from_python_int(3)
    twenty = Number.from_python_int(20)

    sums = [
        "five + three",
        "five - three",
        "three - five",
        "twenty / three",
        "twenty / five"
    ]

    for sum_string in sums:
        print("%s = %s" % (sum_string, str(eval(sum_string))))
