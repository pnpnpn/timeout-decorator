"""Timeout decorator tests."""
from timeout_decorator import timeout
import pytest
import sys
import time


if sys.version_info < (3, 3):             # there is no TimeoutError < Python 3.3
    TimeoutError = AssertionError


@pytest.fixture(params=[False, True])
def use_signals(request):
    """Use signals for timing out or not."""
    return request.param


def test_timeout_decorator_arg(use_signals):
    @timeout(1, use_signals=use_signals)
    def f():
        time.sleep(2)
    with pytest.raises(TimeoutError):
        f()


def test_timeout_class_method(use_signals):
    class c():
        @timeout(1, use_signals=use_signals)
        def f(self):
            time.sleep(2)
    with pytest.raises(TimeoutError):
        c().f()


def test_timeout_kwargs(use_signals):
    @timeout(3, use_signals=use_signals)
    def f():
        time.sleep(2)
    with pytest.raises(TimeoutError):
        f(dec_timeout=1)


def test_timeout_alternate_exception(use_signals):
    @timeout(3, use_signals=use_signals, timeout_exception=StopIteration)
    def f():
        time.sleep(2)
    with pytest.raises(StopIteration):
        f(dec_timeout=1)


def test_timeout_no_seconds(use_signals):
    @timeout(use_signals=use_signals)
    def f():
        time.sleep(0.1)
    f()


def test_timeout_partial_seconds(use_signals):
    @timeout(0.2, use_signals=use_signals)
    def f():
        time.sleep(0.5)
    with pytest.raises(TimeoutError):
        f()


def test_timeout_ok(use_signals):
    @timeout(dec_timeout=2, use_signals=use_signals)
    def f():
        time.sleep(1)
    f()


def test_function_name(use_signals):
    @timeout(dec_timeout=2, use_signals=use_signals)
    def func_name():
        pass

    assert func_name.__name__ == 'func_name'


def test_timeout_pickle_error():
    """Test that when a pickle error occurs a timeout error is raised."""
    @timeout(dec_timeout=1, use_signals=False)
    def f():
        time.sleep(0.1)

        class Test(object):
            pass
        return Test()
    with pytest.raises(TimeoutError):
        f()


def test_timeout_custom_exception_message():
    @timeout(dec_timeout=1, exception_message="Custom fail message")
    def f():
        time.sleep(2)
    with pytest.raises(TimeoutError, match="Custom fail message"):
        f()


def test_timeout_default_exception_message():
    @timeout(dec_timeout=1)
    def f():
        time.sleep(2)
    with pytest.raises(TimeoutError, match="Function f timed out after 1 seconds"):
        f()
