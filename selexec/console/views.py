""":mod:`selexec.console.views` --- Text-based views"""

from selexec.views import MetaApplicationView


class ApplicationView(MetaApplicationView):
    def start(self):
        """Start the application."""
        pass
