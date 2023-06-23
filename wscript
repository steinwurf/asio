#! /usr/bin/env python
# encoding: utf-8

APPNAME = "asio"
VERSION = "2.0.0"


def configure(conf):
    conf.set_cxx_std(11)


def build(bld):
    # Path to the source repo
    directory = bld.dependency_node("asio-source")

    includes = directory.find_node("asio").find_node("include")

    bld(name="asio_includes", export_includes=[includes], use=["ASIO"])

    if bld.is_toplevel():
        bld.recurse("examples")
