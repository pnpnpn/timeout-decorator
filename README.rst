


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
Derived from http://www.saltycrane.com/blog/2010/04/using-python-timeout-decorator-uploading-s3/

Contribute
------------
I would love for you to fork and send me pull request for this project. Please contribute.
