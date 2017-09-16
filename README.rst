Timeout decorator
=================

|Build Status| |Pypi Status| |Coveralls Status|

Installation
------------

From source code:

::

    python setup.py install

From pypi:

::

    pip install timeout-decorator

Usage
-----

::

    import time
    import timeout_decorator

    @timeout_decorator.timeout(5)
    def mytest():
        print 'Start'
        for i in range(1,10):
            time.sleep(1)
            print '%d seconds have passed' % i

    if __name__ == '__main__':
        mytest()

To specify an alternate exception to raise on timeout, first define an exception with a constructor keyword parameter 'value':

::
    class StopIteration(AssertionError):
        def __init__(self, value='Stopped iteration becaue of timeout'):
            self.value = value
            
        def __str__(self):
            return repr(self.value)

Use this exception with the 'timeout_exception' keyword parameter and specify an optional value for the exception's 'value' parameter with the 'timeout' method parameter 'exception_message'. Because decorators are a compile-time code transformation, it is not possible to include runtime values in the exception message.  

::

    import time
    import timeout_decorator

    @timeout_decorator.timeout(5, timeout_exception=StopIteration, 
                                  exception_message='Iteration timed out after 5 seconds')
    def mytest():
        time.sleep(6)
        
    if __name__ == '__main__':
        mytest()

Multithreading
--------------

By default, timeout-decorator uses signals to limit the execution time
of the given function. This appoach does not work if your function is
executed not in a main thread (for example if it's a worker thread of
the web application). There is alternative timeout strategy for this
case - by using multiprocessing. To use it, just pass
``use_signals=False`` to the timeout decorator function:

::

    import time
    import timeout_decorator

    @timeout_decorator.timeout(5, use_signals=False)
    def mytest():
        print "Start"
        for i in range(1,10):
            time.sleep(1)
            print "%d seconds have passed" % i

    if __name__ == '__main__':
        mytest()

.. warning::
    Make sure that in case of multiprocessing strategy for timeout, your function does not return objects which cannot
    be pickled, otherwise it will fail at marshalling it between master and child processes.


Acknowledgement
---------------

Derived from
http://www.saltycrane.com/blog/2010/04/using-python-timeout-decorator-uploading-s3/
and https://code.google.com/p/verse-quiz/source/browse/trunk/timeout.py

Contribute
----------

I would love for you to fork and send me pull request for this project.
Please contribute.

License
-------

This software is licensed under the `MIT license <http://en.wikipedia.org/wiki/MIT_License>`_

See `License file <https://github.com/pnpnpn/timeout-decorator/blob/master/LICENSE.txt>`_

.. |Build Status| image:: https://travis-ci.org/pnpnpn/timeout-decorator.svg?branch=master
   :target: https://travis-ci.org/pnpnpn/timeout-decorator
.. |Pypi Status| image:: https://badge.fury.io/py/timeout-decorator.svg
    :target: https://badge.fury.io/py/timeout-decorator
.. |Coveralls Status| image:: https://coveralls.io/repos/pnpnpn/timeout-decorator/badge.png?branch=master
    :target: https://coveralls.io/r/pnpnpn/timeout-decorator
