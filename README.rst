.. image:: https://travis-ci.org/qcoumes/timeout-decorator.svg?branch=master
    :target: https://travis-ci.org/qcoumes/timeout-decorator
.. image:: https://coveralls.io/repos/github/qcoumes/timeout-decorator/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/qcoumes/timeout-decorator?branch=master
.. image:: https://img.shields.io/badge/python-2.6%2C%202.7%2C%203.2+-brightgreen.svg
    :target: #
.. image:: https://img.shields.io/badge/license-MIT-brightgreen.svg
    :target: https://github.com/qcoumes/timeout-decorator/blob/master/LICENSE

Timeout decorator
=================

Installation
------------

From source code:

::

    python setup.py install

From pip:

::

    pip install -e git://github.com/qcoumes/timeout-decorator.git#egg=timeout-decorator

Usage
-----

::

    import time
    import timeout_decorator

    @timeout_decorator.timeout(5)
    def mytest():
        print("Start")
        for i in range(1,10):
            time.sleep(1)
            print("{} seconds have passed".format(i))

    if __name__ == '__main__':
        mytest()

Specify an alternate exception to raise on timeout:

::

    import time
    import timeout_decorator

    @timeout_decorator.timeout(5, timeout_exception=StopIteration)
    def mytest():
        print("Start")
        for i in range(1,10):
            time.sleep(1)
            print("{} seconds have passed".format(i))

    if __name__ == '__main__':
        mytest()


If used on a non-static method of a class, can use the *timeout* field of the class:

::

    import time
    import timeout_decorator
    
    class Test():
        def __init__(self, timeout):
            self.timeout = timeout
            
        @timeout_decorator.timeout(use_class_attribute=True)
        def mytest(self):
            print("Start")
            for i in range(1,10):
                time.sleep(1)
                print("{} seconds have passed".format(i))

    if __name__ == '__main__':
        Test(5).mytest()



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
            print("{} seconds have passed".format(i))

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
