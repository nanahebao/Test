# encoding=utf-8

from config.conf import logger


def write2file(file, content):
    try:
        with open(file, 'w+') as fd:
            fd.write(content)
            fd.close()
    except Exception as e:
        logger.set_log('Exception:%s'% str(e), level='error')


def read_file(file):
    try:
        with open(file, 'r') as fd:
            content = fd.read()
            fd.close()
        return content
    except Exception as e:
        logger.set_log('Exception:%s' % str(e), level='error')


if __name__ == '__main__':
    #file_name = '/Users/yangcaihua/Documents/Dev/Test/personas/test_positive.json'
    file_name = '../personas/test_positive.json'
    rs = read_file(file_name)
    print(type(rs))
