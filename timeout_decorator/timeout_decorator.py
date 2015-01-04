#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    :copyright: (c) 2012-2013 by PN.
    :license: MIT, see LICENSE for more details.
"""

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import signal
from functools import wraps

############################################################
# Timeout
############################################################

#http://www.saltycrane.com/blog/2010/04/using-python-timeout-decorator-uploading-s3/


class TimeoutError(AssertionError):
    def __init__(self, value="Timed Out"):
        self.value = value

    def __str__(self):
        return repr(self.value)


def timeout(seconds=None):
    def decorate(f):
        def handler(signum, frame):
            raise TimeoutError()

        @wraps(f)
        def new_f(*args, **kwargs):
            old = signal.signal(signal.SIGALRM, handler)

            new_seconds = kwargs['timeout'] if 'timeout' in kwargs else seconds
            if new_seconds is None:
                raise ValueError("You must provide a timeout value")

            signal.alarm(new_seconds)
            try:
                result = f(*args, **kwargs)
            finally:
                signal.signal(signal.SIGALRM, old)
            signal.alarm(0)
            return result
        return new_f
    return decorate
