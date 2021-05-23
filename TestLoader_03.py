# TestLoader
import unittest

# 加法操作
def add(x,y):
    z =x * y
    return z

class Testclo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("======执行一次setUpClass方法======")
    @classmethod
    def tearDownClass(cls) -> None:
        print("======执行一次tearDownClass方法======")
    def setUp(self) -> None:
        print("======执行一次setup方法======")
    def tearDown(self) -> None:
        print("======执行一次tearDown方法======")
    def test_add01(self):
        print("用例1执行完毕")
        self.assertEqual(12,add(3,4))
    def test_add02(self):
        print("用例2执行完毕")
        self.assertEqual(16,add(4,4))
    def test_add03(self):
        print("用例3执行完毕")
        self.assertEqual(8,add(3.5,4.5))

if __name__ == '__main__':
    suite = unittest.TestSuite()
    unittest.main()

#  效果看run_case