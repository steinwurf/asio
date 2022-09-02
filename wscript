#! /usr/bin/env python
# encoding: utf-8

import os
from waflib.extras.wurf.directory import remove_directory

APPNAME = "asio"
VERSION = "1.0.0"


def build(bld):

    # Path to the source repo
    directory = bld.dependency_node("asio-source")

    includes = directory.find_node("asio").find_node("include")
    print(includes)

    bld(name="asio_includes", export_includes=[includes], use=["ASIO"])

    if bld.is_toplevel():

        bld.recurse("examples")
