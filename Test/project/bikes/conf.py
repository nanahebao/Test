# encoding=utf-8

from project.bikes.test_cases.test_bikes import TestBikes

#params needed by suite
#尽量不要在testcase上作skip，除非这个case作废，是否执行通过tests来进行loader
project_name = 'ABTest-UserGroup'

'''
smoking_tests = [TestGroup('test_21_1'),  TestGroup('test_25'),
                 TestGroup('test_26'), TestGroup('test_whitelist')
                 ]
smoking_report = 'reports/smoking_report.html'

main_tests = [TestGroup('test_21_1'), TestGroup('test_21_2'), TestGroup('test_22'),
              TestGroup('test_23'), TestGroup('test_24'), TestGroup('test_25'),
              TestGroup('test_26'), TestGroup('test_whitelist'), TestGroup('test_time_invalid'),
              TestGroup('test_input_lost')
              ]
main_report = 'reports/main_report.html'
'''

full_tests = TestBikes
full_report = 'reports/full_report.html'