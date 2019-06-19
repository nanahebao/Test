# encoding=utf-8


import operator
from lib.data_process import to_json
from config.conf import logger

class ResultCmp():
    def __init__(self, expect_result, actual_result):
        self.expect = to_json(expect_result)
        self.actual = to_json(actual_result)

    def full_cmp(self):
        """compare the full data of result."""
        logger.set_log('compare result using full-cmp...')
        result = operator.eq(self.actual, self.expect)
        logger.set_log('compared result is: %d' % result)
        return result


    def defined_cmp(self):
        """compare the defined key or value of the result."""
        pass

    def include_cmp(self):
        """judge whether expected result be included by actual result"""
        pass

