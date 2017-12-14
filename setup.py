#!/usr/bin/env python
# -*- coding utf-8 -*-

import os

from setuptools import setup


name = 'rt_ip'
version = '0.1'
package = 'rt_ip'
description = 'IP Middleware for Django'
author = 'Thibault Ravera'
author_email = 'ravera.thibault@gmail.com'
licence = 'MIT'
install_requires = []


def get_packages(package):
    """
    Return root package and all sub-packages

    :return: List of packages
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in package themselves.

    :param package:
    :return:
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


setup(name=name,
      version=version,
      licence=licence,
      description=description,
      author=author,
      author_email=author_email,
      packages=get_package_data(package),
      package_data=get_package_data(package),
      install_requires=install_requires)