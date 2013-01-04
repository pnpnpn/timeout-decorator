


Installation
------------
From source code: ::

    python setup.py install

From pypi: ::

    pip install timeout-decorator

Usage
-----
::

    import time
    import timeout_decorator 

    @timeout_decorator.timeout(5)
    def mytest():
        print "Start"
        for i in range(1,10):
            time.sleep(1)
            print "%d seconds have passed" % i

    if __name__ == '__main__':
        mytest()


Acknowledgement
--------------------
Derived from http://pyparsing.wikispaces.com/file/view/streetAddressParser.py
