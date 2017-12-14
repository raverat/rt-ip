#!/usr/bin/env python

from __future__ import print_function

import pytest

import os
import subprocess
import sys


PYTEST_ARGS = {
    'default': ['tests'],
    'fast': ['tests', '-q']
}


sys.path.append(os.path.dirname(__file__))


def exit_on_failure(ret, message=None):
    if ret:
        sys.exit(ret)


if __name__ == '__main__':
    try:
        sys.argv.remove('--fast')
    except ValueError:
        style = 'default'
    else:
        style = 'fast'

    if len(sys.argv) > 1:
        pytest_args = sys.argv[1:]
        first_arg = pytest_args[0]

        try:
            pytest_args.remove('--coverage')
        except ValueError:
            pass
        else:
            pytest_args = ['--cov-report',
                           'xml',
                           '--cov',
                           'rt_ip'] + pytest_args

        if first_arg.startswith('-'):
            # `runtests.py [flags]`
            pytest_args = ['tests'] + pytest_args

    else:
        pytest_args = PYTEST_ARGS[style]

    exit_on_failure(pytest.main(pytest_args))
