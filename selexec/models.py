""":mod:`selexec.models` --- Application Models"""

import sys
import argparse
from abc import ABCMeta, abstractmethod, abstractproperty

from selexec.utils import Event
from selexec import metadata


class MetaApplicationModel(object):
    __metaclass__ = ABCMeta

    started = Event()
    """Fired when the application starts."""

    @abstractmethod
    def run(self, argv):
        """Start the application.

        :param argv: argument vector
        :type argv: :class:`list`
        """
        raise NotImplementedError()

    def list_items(self):
        """Return a list of items provided on stdin.

        :return: list of items
        :rtype: :class:`list` of :class:`str`
        """
        raise NotImplementedError()


class ApplicationModel(MetaApplicationModel):
    def run(self, argv):
        if argv is None:
            argv = sys.argv

        author_strings = []
        for name, email in zip(metadata.authors, metadata.emails):
            author_strings.append('Author: {0} <{1}>'.format(name, email))

        version_str = '{0} {1}'.format(metadata.nice_title, metadata.version)
        epilog = '''
{version_str}

{authors}
URL: <{url}>
'''.format(
            title=metadata.nice_title,
            version_str=version_str,
            authors='\n'.join(author_strings),
            url=metadata.url)

        arg_parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=metadata.description,
            epilog=epilog)
        arg_parser.add_argument('--version', '-V',
                                action='version', version=version_str)

        args = arg_parser.parse_args(args=argv[1:])

        self.started()

    def list_items(self):
        return sys.stdin.read().splitlines(False)
