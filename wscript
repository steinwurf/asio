#! /usr/bin/env python
# encoding: utf-8

APPNAME = "asio"
VERSION = "1.1.0"


def build(bld):

    # Path to the source repo
    directory = bld.dependency_node("asio-source")

    includes = directory.find_node("asio").find_node("include")

    bld(name="asio_includes", export_includes=[includes], use=["ASIO"])

    if bld.is_toplevel():

        bld.recurse("examples")
