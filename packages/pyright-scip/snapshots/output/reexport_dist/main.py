# < definition scip-python python snapshot-util 0.1 main/__init__:

from clk import Context, Top
#    ^^^ reference  clk 2.0 clk/__init__:
#               ^^^^^^^ reference  clk 2.0 `clk.core`/Context#
#                        ^^^ reference  clk 2.0 clk/Top#
from clk import core
#    ^^^ reference  clk 2.0 clk/__init__:
#               ^^^^ reference  clk 2.0 `clk.core`/__init__:
from clk.core import Context as CoreContext
#    ^^^^^^^^ reference  clk 2.0 `clk.core`/__init__:
#                    ^^^^^^^^^^^^^^^^^^^^^^ reference  clk 2.0 `clk.core`/Context#

Context().run()
#^^^^^^ reference  clk 2.0 `clk.core`/Context#
#         ^^^ reference  clk 2.0 `clk.core`/Context#run().
Top().go()
#^^ reference  clk 2.0 clk/Top#
#     ^^ reference  clk 2.0 clk/Top#go().
core.Context().run()
#^^^ reference  clk 2.0 `clk.core`/__init__:
#    ^^^^^^^ reference  clk 2.0 `clk.core`/Context#
#              ^^^ reference  clk 2.0 `clk.core`/Context#run().
CoreContext().run()
#^^^^^^^^^^ reference  clk 2.0 `clk.core`/Context#
#             ^^^ reference  clk 2.0 `clk.core`/Context#run().

