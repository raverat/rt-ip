#!/usr/bin/env python

from __future__ import print_function

import pytest

import os
import subprocess
import sys


PYTEST_ARGS = {
    'default': ['tests'],
}


sys.path.append(os.path.dirname(__file__))


def exit_on_failure(ret, message=None):
    if ret:
        sys.exit(ret)


if __name__ == '__main__':
    pytest_args = PYTEST_ARGS['default'] + ['-s']
    exit_on_failure(pytest.main(pytest_args))
