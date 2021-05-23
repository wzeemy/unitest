import unittest
from parameterized import parameterized

def add(x,y):
    z =x + y
    return z



version = 1.3

class Testclo(unittest.TestCase):


    def test_add01(self):
        print("用例1执行完毕")
        res1 = add(3,4)
        self.assertEqual(7,res1)

    @unittest.skip('测试跳过函数')
    def test_add02(self):
        print("用例2执行完毕")
        res2 = add(4,0)
        self.assertEqual(4,res2)

    @unittest.skipIf(version > 1.2,'旧版本已修复此bug')
    def test_add03(self):
        print("用例3执行完毕")
        res3 = add(-1,3)
        self.assertEqual(22,res3)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    unittest.main()

