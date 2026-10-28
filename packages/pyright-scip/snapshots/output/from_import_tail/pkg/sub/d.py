# < definition scip-python python snapshot-util 0.1 `pkg.sub.d`/__init__:

from ..c import g
#    ^^^ reference  snapshot-util 0.1 `pkg.c`/__init__:
#               ^ reference  snapshot-util 0.1 `pkg.c`/g().
from .. import c
#    ^^ reference local 0
#              ^ reference  snapshot-util 0.1 `pkg.c`/__init__:
from . import b
#    ^ reference local 1
#             ^ reference  snapshot-util 0.1 `pkg.sub.b`/__init__:

g()
# reference  snapshot-util 0.1 `pkg.c`/g().
c.g()
# reference  snapshot-util 0.1 `pkg.c`/__init__:
# ^ reference  snapshot-util 0.1 `pkg.c`/g().
b.f()
# reference  snapshot-util 0.1 `pkg.sub.b`/__init__:
# ^ reference  snapshot-util 0.1 `pkg.sub.b`/f().

