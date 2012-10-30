from mock import create_autospec, sentinel

from selexec.models import MetaApplicationModel
from selexec.views import MetaApplicationView
from selexec.presenters import ApplicationPresenter


def pytest_funcarg__presenter(request):
    mock_model = create_autospec(MetaApplicationModel, spec_set=True)
    mock_view = create_autospec(MetaApplicationView, spec_set=True)
    presenter = ApplicationPresenter(mock_model, mock_view)
    return presenter


class TestPresenters:
    def test_register_for_events(self, presenter):
        """When the application starts, the presenter registers for
        events fired by the view and the model."""
        presenter.register_for_events()
        presenter.model.started.append.assert_called_once_with(
            presenter.view.start)
