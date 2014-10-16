


Installation
------------
From source code:

    python setup.py install

From pypi:

    pip install timeout-decorator

Usage
-----


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

License
---------
The MIT License (MIT)

Copyright (c) 2012-2014 Patrick Ng

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
