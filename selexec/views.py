""":mod:`selexec.views` --- View abstract base classes"""

from abc import ABCMeta, abstractmethod

from selexec.utils import Event


class MetaApplicationView(object):
    __metaclass__ = ABCMeta

    items_listed = Event()
    """Fired when a list of items needs to be shown."""

    @abstractmethod
    def start(self):
        """Called when the application is started."""
        raise NotImplementedError()

    @abstractmethod
    def show_items(self, items):
        """Show the user the list of available items

        :param items: the list of items
        :type items: :class:`list`
        """
        raise NotImplementedError()
