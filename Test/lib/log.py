# encoding=utf-8
import logging.config
import os
#import config.conf
import yaml

log_name = 'my_module'
LOG_CFG = 'logging.yaml'
#LOG_CFG = conf.LOG_CFG
print(LOG_CFG)


# 通过配置文件来配置log--可是如何使用？
class Logger:
    def __init__(self, name, path='/Users/ln/PycharmProjects/FF/config/logging.yaml', default_level=logging.INFO, env_key=LOG_CFG):
        #path = 'logging.yaml'
        #env_key = 'LOG_CFG'
        """

        :rtype: object
        """
        #name = __name__
        value = os.getenv(env_key, None)
        # print(value)
        # print('---path....', path)
        if value:
            path = value
        if os.path.exists(path):
            # print('----')
            with open(path, 'rt') as f:
                config = yaml.load(f)
            logging.config.dictConfig(config)

        else:
            logging.basicConfig(level=default_level)

        self.logger = logging.getLogger(name)

    def set_log(self, message, level='info'):
        _level = {
            "debug": self.logger.debug,
            "info": self.logger.info,
            "warn": self.logger.warning,
            "error": self.logger.error,
            "critical": self.logger.critical
        }

        _level[level](message)

        #return self.logger
        #pass


if __name__ == '__main__':
    logger = Logger(log_name)
    logger.set_log('test')

    logger.set_log('error', level='error')
    logger.set_log('war', level='warn')
    logger.set_log('debug', level='debug')
    # logger.get_logger()
#