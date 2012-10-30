""":mod:`selexec.console.views` --- Text-based views"""

from __future__ import print_function

from selexec.views import MetaApplicationView
from texttable import Texttable


class ApplicationView(MetaApplicationView):
    def start(self):
        self.items_listed()

    def show_items(self, items):
        table = Texttable(max_width=0)
        table.header(['#', 'item'])
        table.set_deco(Texttable.HEADER | Texttable.VLINES)
        table.set_cols_dtype(['i', 't'])
        table.add_rows([(i, item) for i, item in enumerate(items)],
                       header=False)
        print(table.draw())
