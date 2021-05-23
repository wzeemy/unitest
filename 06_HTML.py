"""
1. 复制HTMLTestRunner.py文件到项目文件夹
2. 导入HTMLTestRunner、unittest包
3. 生成测试套件
suite = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
4. 设置报告生成路径和文件名
file_name = "./test_report.html"
5. 打开报告 with open(file_name,'wb') as f:
6. 实例化HTMLTestRunner对象：
runner = HTMLTestRunner(stream=f,[title],[description])
参数说明：
stream：文件流，打开写入报告的名称及写入编码格式)
title：[可选参数]，为报告标题，如XXX自动化测试报告
description：[可选参数]，为报告描述信息；比如操作系统、浏览器等版本
7. 执行：runner.run(suite)
"""