# encoding=utf-8
import unittest
from lib.HTMLTestRunner2 import HTMLTestRunner


def suite_func(tests, report, tag, project_name, title='Automation test report'):
    suite = unittest.TestSuite()
    if tag == 3:
        print('coming-----')
        tests = [unittest.TestLoader().loadTestsFromTestCase(tests)]

    suite.addTests(tests)
    _type = {
        1: 'smoking',
        2: 'main function',
        3: 'full regression'
    }
    with open(report, 'w+') as f:
        runner = HTMLTestRunner(stream=f,
                                title=title,
                                description='This is a %s test report of %s'%(_type[tag], project_name),
                                verbosity=2
                                )
        runner.run(suite)
        f.close()

