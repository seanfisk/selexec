""":mod:`selexec.presenters` --- Application presenters"""


class ApplicationPresenter(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def register_for_events(self):
        """Register the presenter for model and view events."""
        self.model.started.append(self.view.start)
        self.view.items_listed.append(self._list_items)

    def _list_items(self):
        """Show the user a list of available items."""
        self.view.show_items(self.model.list_items())
