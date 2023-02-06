# timeoutd

[![Build
Status](https://travis-ci.org/pnpnpn/timeout-decorator.svg?branch=master)](https://travis-ci.org/pnpnpn/timeout-decorator)
[![Pypi
Status](https://badge.fury.io/py/timeout-decorator.svg)](https://badge.fury.io/py/timeout-decorator)
[![Coveralls
Status](https://coveralls.io/repos/pnpnpn/timeout-decorator/badge.png?branch=master)](https://coveralls.io/r/pnpnpn/timeout-decorator)

## Installation

From source code:

```shell
pip install -e .
```

From pypi:

```shell
pip install timeoutd
```

## Usage

```python
    import time
    import timeoutd

    @timeoutd.timeout(5)
    def mytest():
        print("Start")
        for i in range(1,10):
            time.sleep(1)
            print(f"{i} seconds have passed")

    if __name__ == '__main__':
        mytest()
```

Specify an alternate exception to raise on timeout:

```python
    import time
    import timeoutd

    @timeoutd.timeout(5, timeout_exception=StopIteration)
    def mytest():
        print("Start")
        for i in range(1,10):
            time.sleep(1)
            print(f"{i} seconds have passed")

    if __name__ == '__main__':
        mytest()

```

### Multithreading

_Note:_ This feature appears to be broken in some cases for the original timeout-decorator.
Some issues might still exist in this fork.

By default, `timeoutd` uses signals to limit the execution time of the given function.
This approach does not work if your function is executed not in a main thread (for example if it's a worker thread of the web application).
There is alternative timeout strategy for this case - by using multiprocessing.
To use it, just pass `use_signals=False` to the timeout decorator function:

```python
    import time
    import timeoutd

    @timeoutd.timeout(5, use_signals=False)
    def mytest():
        print "Start"
        for i in range(1,10):
            time.sleep(1)
            print("{} seconds have passed".format(i))

    if __name__ == '__main__':
        mytest()
```

_Warning:_
Make sure that in case of multiprocessing strategy for timeout, your function does not return objects which cannot be pickled, otherwise it will fail at marshalling it between master and child processes.

## Acknowledgement

Derived from
<http://www.saltycrane.com/blog/2010/04/using-python-timeout-decorator-uploading-s3/>, <https://code.google.com/p/verse-quiz/source/browse/trunk/timeout.py>, and <https://github.com/pnpnpn/timeout-decorator>
