# < definition scip-python python snapshot-util 0.1 `pkg.a`/__init__:

from .sub.b import f
#    ^^^^^^ reference  snapshot-util 0.1 `pkg.sub.b`/__init__:
#                  ^ reference  snapshot-util 0.1 `pkg.sub.b`/f().
from . import c
#    ^ reference local 0
#             ^ reference  snapshot-util 0.1 `pkg.c`/__init__:
from .c import g
#    ^^ reference  snapshot-util 0.1 `pkg.c`/__init__:
#              ^ reference  snapshot-util 0.1 `pkg.c`/g().

f()
# reference  snapshot-util 0.1 `pkg.sub.b`/f().
c.g()
# reference  snapshot-util 0.1 `pkg.c`/__init__:
# ^ reference  snapshot-util 0.1 `pkg.c`/g().
g()
# reference  snapshot-util 0.1 `pkg.c`/g().

