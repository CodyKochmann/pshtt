# -*- coding: utf-8 -*-
# @Author: Cody Kochmann
# @Date:   2017-07-08 14:30:24
# @Last Modified by:   Cody Kochmann
# @Last Modified time: 2017-07-08 14:49:11

def logged(fn):
    def wrapper(*a,**k):
        print("called {} - {}{}".format(fn.__name__,a,k))
        out = fn(*a,**k)
        print("output - {}".format(out))
        return out
    return wrapper

if __name__ == '__main__':

    @logged
    def test(hi):
        print('test is running')

    test('hello')

