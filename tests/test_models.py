from mock import patch, MagicMock

from selexec.models import ApplicationModel
from selexec import metadata


def pytest_funcarg__model(request):
    return ApplicationModel()


def pytest_generate_tests(metafunc):
    if 'helparg' in metafunc.funcargnames:
        metafunc.parametrize('helparg', ['-h', '--help'])
    elif 'versionarg' in metafunc.funcargnames:
        metafunc.parametrize('versionarg', ['-V', '--version'])


class TestModels:
    class TestRun:
        # capfd argument allows capture of stdout/stderr based on file
        # descriptors
        # see <http://pytest.org/latest/capture.html> for more information
        def test_help(self, model, helparg, capfd):
            """When the user passes in `-h' or `--help' as an
            argument, they should be shown the program usage.
            """
            with patch('sys.exit') as mock_exit:
                model.run(['progname', helparg])
            out, err = capfd.readouterr()
            # some basic tests to check output
            assert 'usage' in out
            assert 'Author' in out
            assert 'URL'in out
            mock_exit.assert_called_once_with(0)

        def test_help_sys_argv(self, model, helparg, capfd):
            """When `None' is given as argv to run(), the arguments
            should be read from `sys.argv'.
            """
            with patch('sys.argv', ['progname', helparg]):
                with patch('sys.exit') as mock_exit:
                    model.run(None)
            out, err = capfd.readouterr()
            # some basic tests to check output
            assert 'usage' in out
            assert 'Author' in out
            assert 'URL'in out
            mock_exit.assert_called_once_with(0)

        def test_version(self, model, versionarg, capfd):
            with patch('sys.exit') as mock_exit:
                model.run(['progname', versionarg])
            out, err = capfd.readouterr()
            # some basic tests to check output
            assert err == '{0} {1}\n'.format(metadata.nice_title,
                                             metadata.version)
            mock_exit.assert_called_once_with(0)

        def test_started_called(self, model):
            started_callback = MagicMock()
            model.started.append(started_callback)
            model.run(['progname'])
            started_callback.assert_called_once_with()

    class TestListItems:
        def test_empty(self, model):
            items = ''
            with patch('sys.stdin') as mock_stdin:
                mock_stdin.read.return_value = items
                computed = model.list_items()
            mock_stdin.read.assert_called_once_with()
            assert computed == []

        def test_empty_lines(self, model):
            items = '\n\n\n'
            with patch('sys.stdin') as mock_stdin:
                mock_stdin.read.return_value = items
                computed = model.list_items()
            mock_stdin.read.assert_called_once_with()
            assert computed == ['', '', '']

        def test_simple(self, model):
            items = '''this
is
a
fake
list'''
            with patch('sys.stdin') as mock_stdin:
                mock_stdin.read.return_value = items
                computed = model.list_items()
            mock_stdin.read.assert_called_once_with()
            assert computed == ['this', 'is', 'a', 'fake', 'list']

        def test_long_strange_spaces(self, model):
            items = ('  this   \n'
                     '  is fdsafd &&&^   \n'
                     '\ta hello\n'
                     'fake\t\n'
                     'spacious\n'
                     '\n'
                     'list ha\n')
            with patch('sys.stdin') as mock_stdin:
                mock_stdin.read.return_value = items
                computed = model.list_items()
                mock_stdin.read.assert_called_once_with()
                assert computed == [
                    '  this   ',
                    '  is fdsafd &&&^   ',
                    '\ta hello',
                    'fake\t',
                    'spacious',
                    '',
                    'list ha'
                ]
