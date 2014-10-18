#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from nose.tools import raises

from timeout_decorator import timeout, TimeoutError


@raises(TimeoutError)
def test_timeout_decorator_arg():
    @timeout(1)
    def f():
        time.sleep(2)
    f()


@raises(TimeoutError)
def test_timeout_kwargs():
    @timeout()
    def f(timeout):
        time.sleep(2)
    f(timeout=1)


@raises(ValueError)
def test_timeout_no_seconds():
    @timeout()
    def f(timeout):
        time.sleep(2)
    f()


def test_timeout_ok():
    @timeout(seconds=2)
    def f():
        time.sleep(1)
    f()


def test_function_name():
    @timeout(seconds=2)
    def func_name():
        pass

    assert func_name.__name__ == 'func_name'
