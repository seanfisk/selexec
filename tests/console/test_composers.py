from mock import patch, sentinel, call

from selexec.console.composers import create_application_presenter


class TestComposers:
    @patch('selexec.console.composers.ApplicationPresenter',
           autospec=True, spec_set=True)
    @patch('selexec.console.composers.ApplicationView',
           autospec=True, spec_set=True)
    @patch('selexec.console.composers.ApplicationModel',
           autospec=True, spec_set=True)
    def test_create_application_presenter(self, mock_model,
                                          mock_view, mock_presenter):
        model = mock_model.return_value
        mock_view.return_value = sentinel.view
        presenter = mock_presenter.return_value

        retval = create_application_presenter(sentinel.args)
        assert retval == presenter

        mock_view.assert_called_once_with()
        expected_model_calls = call().run(sentinel.args).call_list()
        expected_presenter_calls = call(model, sentinel.view).\
            register_for_events().call_list()
        assert mock_model.mock_calls == expected_model_calls
        assert mock_presenter.mock_calls == expected_presenter_calls
