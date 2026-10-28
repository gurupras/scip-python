# < definition scip-python python snapshot-util 0.1 main/__init__:

from this_is_not_real.sub import Thing
#    ^^^^^^^^^^^^^^^^^^^^ reference local 0
#                                ^^^^^ reference local 1
from _typeshed import StrPath
#    ^^^^^^^^^ reference  python-stdlib 3.11 _typeshed/__init__:
#                     ^^^^^^^ reference local 2

Thing()
#^^^^ reference local 1


def open_it(p: StrPath):
#   ^^^^^^^ definition  snapshot-util 0.1 main/open_it().
#           ^ definition  snapshot-util 0.1 main/open_it().(p)
#              ^^^^^^^ reference local 2
    return p
#          ^ reference  snapshot-util 0.1 main/open_it().(p)

