# encoding=utf-8

from project.personas.test_cases.test_positive import TestGetConfig

#params needed by suite
#尽量不要在testcase上作skip，除非这个case作废，是否执行通过tests来进行loader
project_name = 'personas'

smoking_tests = [TestGetConfig('test1'), TestGetConfig('test_get_config')]
smoking_report = 'reports/smoking_report.html'

main_tests = [TestGetConfig('test1'), TestGetConfig('test_get_config')]
main_report = 'reports/main_report.html'

full_tests = TestGetConfig
full_report = 'reports/full_report.html'
