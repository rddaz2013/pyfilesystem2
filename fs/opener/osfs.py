# coding: utf-8
"""Defines the OSFSOpener."""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from .base import Opener

class OSFSOpener(Opener):
    protocols = ['file', 'osfs']

    def open_fs(self, fs_url, parse_result, writeable, create, cwd):
        from ..osfs import OSFS
        from os.path import abspath, normpath, join
        _path = abspath(join(cwd, parse_result.resource))
        path = normpath(_path)
        osfs = OSFS(path, create=create)
        return osfs
