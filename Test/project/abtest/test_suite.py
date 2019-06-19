# encoding=utf-8
import unittest

from lib.suite_func import suite_func
from lib.HTMLTestRunner import HTMLTestRunner
from project.abtest.conf import *
from project.personas.test_cases.test_positive import TestGetConfig


def test_smoking_suite():
    tests = smoking_tests
    report = smoking_report
    project = project_name
    suite_func(tests, report, 1, project)


def test_main_suite():
    tests = main_tests
    report = main_report
    project = project_name
    suite_func(tests, report, 2, project)


def test_full_suite():
    tests = full_tests
    report = full_report
    project = project_name
    suite_func(tests, report, 3, project)


def test_other_suite():
    pass


if __name__ == '__main__':
    #test_smoking_suite()
    test_full_suite()


    suite = unittest.TestSuite()

    tests = [TestGetConfig('test1'), TestGetConfig('test_get_config')]
    suite.addTests(tests)
    with open('report.html', 'w+') as f:
        runner = HTMLTestRunner(stream=f,
                                title='a test report',
                                description='This is a test report of %s'%project_name,
                                verbosity=2)
        # runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)
        f.close()



