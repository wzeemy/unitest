import unittest

# 加法操作
def add(x,y):
    z =x +y
    return z

# 最原始的测试方法
print(add(3,4) == 7)
print(add(3,4) == 6)

# testcase 方法
# 断言就是两个值进行比较,测试断言就是指预期结果和实际结果进行比较
class TestAdd(unittest.TestCase):         # --  大写Test开头  继承类
    @classmethod                          # 装饰器
    def setUpClass(cls) -> None:
        print("===================执行一次setUpClass方法===========")
    @classmethod
    def tearDownClass(cls) -> None:
        print("===================执行一次tearDownClass方法===========")
    def setUp(self) -> None:
        print("===================执行一次setup方法================")
    def tearDown(self) -> None:
        print("==================执行一次tearDown方法==============")
    def test_add01(self):                 # 小写test
        print("用例1执行完毕")
        self.assertEqual(7,add(3,4))
    def test_add02(self):
        print("用例2执行完毕")
        self.assertEqual(6,add(3,4))
    def test_add03(self):
        print("用例3执行完毕")
        self.assertEqual(8,add(3.5,4.5))           # --  三个测试用例

if __name__ == '__main__':
    unittest.main()

# assertEqual(a,b)           a ==b
# assertNotEqual(a,b)        a!=b
# assertTrue(x)              bool(x) is True
# assertFalse(x)             bool(x) is False
# assertIs(a,b)              a is b
# assertIsNot(a,b)           a is not b
# assertIsNone(x)            x is None
# assertIsNotNone(x)         x is not None
# assertIn(a,b)              a in b
# assertNotIn(a,b)           a not in
# assertIsInstance(a,b)      isinstance(a,b)
# assertNotIsInstance(a,b)   not isinstance(a,b)
# assertGreater(a,b)         a>b
# assertGreaterEqual(a,b)    a>=b
# assertLess(a,b)            a<b
# assertLessEqual(a,b)       a<=b

# 初始化和清除方法
# 方法                    说明                    使用场景
# setUp()              初始化方法            如果每次运行测试方法前都需要先执行setup()
# tearDown()           清空方法             如果每次运行测试方法后都需要先执行tearDown()
# setUpClass()         bool(x) is True     整个类在运行前，先运行setupClass()
# tearDownClass()       bool(x) is False    整个类在运行结束时，先运行tearDownClass()

# setupclass → setup → a用例 → tearDown → setup → b → tearDown → tearDownClass