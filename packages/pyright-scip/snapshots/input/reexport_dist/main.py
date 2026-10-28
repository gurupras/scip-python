from clk import Context, Top
from clk import core
from clk.core import Context as CoreContext

Context().run()
Top().go()
core.Context().run()
CoreContext().run()
