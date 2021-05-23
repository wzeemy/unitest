import unittest
from parameterized import parameterized

def add(x,y):
    z =x + y
    return z

class Testclo(unittest.TestCase):

    data = [(7,3,4),(4,0,4),(3,-3,6),(6,2.5,3.5),(3,2,4),(3,2,'')]
    @parameterized.expand(data)
    def test_add(self,c,a,b):
        res = add(a,b)
        self.assertEqual(c,res)

    # def test_add01(self):
    #     print("用例1执行完毕")
    #     res1 = add(3,4)
    #     self.assertEqual(7,res1)
    # def test_add02(self):
    #     print("用例2执行完毕")             -- 使用参数化代替
    #     res2 = add(4,0)
    #     self.assertEqual(4,res2)
    # def test_add03(self):
    #     print("用例3执行完毕")
    #     res3 = add(-1,3)
    #     self.assertEqual(22,res3)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    unittest.main()

