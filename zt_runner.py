#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

if __name__ == '__main__':

    MASK = 'zt_'
    count = 0
    errors = 0
    fails = 0

    runner = unittest.TextTestRunner(verbosity=0)
    loader = unittest.TestLoader()
    suites = loader.discover('./ztest', pattern='%s*.py' % MASK)
    for suite in suites:
        result = runner.run(suite)
        errors += len(result.errors)
        fails += len(result.failures)
        count += suite.countTestCases()

    runner.stream.writeln('%s tests, %s errors %s fails' % (count, errors, fails))
