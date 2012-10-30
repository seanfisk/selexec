""":mod:`selexec.presenters` --- Application presenters"""


class ApplicationPresenter(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def register_for_events(self):
        """Register the presenter for model and view events."""
        self.model.started.append(self.view.start)
