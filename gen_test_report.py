# 1.拷贝HTML文件进该项目下

# 2.导入HTML和unittest
from HTMLTestRunner import HTMLTestRunner
import unittest

# 3.定义一个测试报告的文件
report_file = "./test_report.html"

# 4.创建套件
suite = unittest.TestLoader().discover('.',pattern='test*.py')

# 5.生成一个runner运行器
with open(report_file,'wb') as f:
    runner = HTMLTestRunner(f,title='测试报告',description='v1.2版本')
    runner.run(suite)

# 会在项目下自动生成.html文件,在浏览器中打开即可查看报告



























