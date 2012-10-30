""":mod:`selexec.console.composers` --- Console composers"""

from selexec.models import ApplicationModel
from selexec.console.views import ApplicationView
from selexec.presenters import ApplicationPresenter


def create_application_presenter(argv):
    """Create the console application presenter.

    :return: the app presenter
    :rtype: :class:`ApplicationPresenter`
    """
    model = ApplicationModel()
    view = ApplicationView()
    presenter = ApplicationPresenter(model, view)
    presenter.register_for_events()
    model.run(argv)
    return presenter
