#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
