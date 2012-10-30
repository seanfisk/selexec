#!/usr/bin/env python
""":mod:`selexec.console.main` -- Pure text-based main
"""

from selexec.console.composers import create_application_presenter


def main(argv=None):
    presenter = create_application_presenter(argv)

if __name__ == '__main__':
    main()
