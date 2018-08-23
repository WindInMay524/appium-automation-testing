import unittest
import sys
import os
#sys.path.append("..")
'''
from case.Test001_RefuseSaleManagerRegister import TestRefuseSaleManagerRegister
from case.Test002_ApproveSaleManagerRegister import TestApproveSaleManagerRegister
from case.Test003_RefuseCustomerRegister import TestRefuseCustomerRegister
from case.Test004_ApproveCustomerRegister import TestApproveCustomerRegister
from case.Test005_RefuseShopKeeperRegisterByOperation import TestRefuseShopKeeperRegisterByOperation
from case.Test006_RefuseShopKeeperRegisterByCustomer import TestRefuseShopKeeperRegisterByCustomer
from case.Test007_ApproveShopKeeperRegister import TestApproveShopKeeperRegister
'''
from common import CommonConfiguration as cc
from common import HTMLTestRunner
#from common import SendEmail

if os.path.exists(cc.folderPath()):
    print('The folder has already existed')
else:
    os.makedirs(cc.folderPath())
test_suite_dir = '%s/case/' % (os.path.dirname(os.path.abspath(__file__))) #case存放路径
def createsuite():
    testunit = unittest.TestSuite()
    package_tests = unittest.defaultTestLoader.discover(test_suite_dir,
                                                        pattern = 'Test*.py',
                                                        top_level_dir=None)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in package_tests:
        for test_case in test_suite:
            testunit.addTests(test_case)
    print(testunit)

    return testunit

alltestnames = createsuite()

if __name__ == '__main__':
#    suite = unittest.TestSuite()
#    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestRefuseSaleManagerRegister))
#    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestApproveSaleManagerRegister))
 #   suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestRefuseCustomerRegister))
  #  suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestApproveCustomerRegister))
   # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestRefuseShopKeeperRegisterByOperation))
#    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestRefuseShopKeeperRegisterByCustomer))
    #suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestApproveShopKeeperRegister))
    with open('%s/HTMLReport.html' % cc.folderPath(), 'wb') as f:
        HTMLTestRunner.HTMLTestRunner(stream=f,
               title=u'北京中维公众号自动化测试报告',
               description=u'测试用例执行结果',
               verbosity=2).run(alltestnames)
    f.close()

#SendEmail.zip_folder()
#SendEmail.mail()


