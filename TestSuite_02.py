# TestSuit 测试套件
# addTest(test):添加一个TestCase或TestSuite到套件中。
# addTests(test):把TestCase和TestSuite中给的所有的测试实例添加到套件中。

import unittest
from TestCace_01 import TestAdd
suite = unittest.TestSuite()
suite.addTest(TestAdd('test_add01'))
runner = unittest.TextTestRunner()
runner.run(suite)


# TextTestRunner
# 一个基础的测试用例执行器，实现了将结果输出为流的功能。如果stream为None，默认的，sys.stderr会被作为输出流。
#  run(suite)：运行测试套件，并收集结果信息传递给测试报告对象


















