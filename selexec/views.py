""":mod:`selexec.views` --- View abstract base classes"""

from abc import ABCMeta, abstractmethod


class MetaApplicationView(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def start(self):
        """Called when the application is started."""
        raise NotImplementedError()
