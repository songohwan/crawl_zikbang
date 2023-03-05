'''
Python 예제 400문제
Class Example
'''

import math
class makecircle():
    def __init__(self, r):
        self.r = r
        self.mkcircle()
        self.mkline()
    def mkcircle(self):
        self.area = math.pi * self.r
    def mkline(self):
        self.line = 2 * self.r * math.pi
    def __str__(self):
        return 'area = {}, line = {}'.format(self.area, self.line)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = makecircle(10)
    print(a)