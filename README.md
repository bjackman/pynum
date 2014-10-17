pynum
=====

In `number.py` is a class called Number that implements positive integer arithmetic in pure python. It implements functions like `__add__()` and `__sub__()` so you can use the normal arithmetic operators on them. It then uses its own implementation of arithmetic to provide conversion to and from strings.

I haven't commented it very well, but if with a bit of effort it's quite easy to understand. Basically it forms a long doubly linked list of predecessors and successors that grows dynamically as required. It's rampantly recursive and makes no attempt at scalability or performance - it's just a bit of fun.

Why not fork it and add more features? Negative numbers? Rational numbers? Imaginary numbers? The software world clearly needs pure Python implementations of these things!
