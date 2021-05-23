import unittest

# 用TestLoader方法搜索用例测试

# 生成一个套件对象
suite = unittest.TestLoader().discover('.',pattern='test*.py')
runner = unittest.TextTestRunner()
runner.run(suite)