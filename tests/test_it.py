import unittest

from needle import ninh


count = 0


def create_func(func, *args, **kwargs):
    global count

    def new_func(self):
        return func(self, *args, **kwargs)
    new_func.__name__ = "test_{0}_{1}".format(func.__name__, count)
    count += 1
    return new_func.__name__, new_func


class TestNinh(unittest.TestCase):
    def ninh_check(self, needle, haystack, expected):
            result = ninh(needle, haystack)
            self.assertEqual(result, expected)

all_args = [
    ('', '', ''),
    ('XXXXXXX', 'abc', None),
    ('XXXabXX', 'abc', None),
    ('abc', 'abc', 'abc'),
    ('cab', 'abc', 'cab'),
    ('bca', 'abc', 'bca'),
    ('XaXbXcX', 'abc', 'aXbXc'),
    ('XcXaXbX', 'abc', 'cXaXb'),
    ('XbXcXaX', 'abc', 'bXcXa'),
    ('XaXcaaX', 'aac', 'caa'),
    ('XaXcXaX', 'aac', 'aXcXa'),
    ('XaXcXbXaXXbXXcXcXXXbXXXa', 'abc', 'aXcXb'),
    ('XaXXbXXcXaXcXbXcXXXbXXXa', 'abc', 'aXcXb'),
    ('XcXXXbXXXaXaXXbXXcXaXcXb', 'abc', 'aXcXb'),
    ('XaXXbXXaXXaXXcX', 'abc', 'bXXaXXaXXc')]
for haystack, needle, expected in all_args:
    setattr(TestNinh, *create_func(
        TestNinh.ninh_check, needle=needle, haystack=haystack,
        expected=expected))
