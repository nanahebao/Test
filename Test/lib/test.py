import sys
from config.conf import logger



def test_log():
    print('come in')
    logger.set_log('test123', 'info')





if __name__ == '__main__':
    test_log()