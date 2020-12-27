import time
import logging
import os

def test_log():
    current_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    dir_path = r'C:\Python006-006\week01\python-{}'.format(current_time)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    logging.basicConfig(filename=r'{}\test_log.log'.format(dir_path),
                        level=logging.DEBUG,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        format='%(asctime)s - [line:%(lineno)d] - %(filename)s - %(levelname)s: %(message)s')
    logging.info('info message')
    logging.debug('Localtime time is:{}'.format(time.localtime()))
    logging.debug('Current time is:{}'.format(current_time))
    logging.debug('Log path is: {}'.format(dir_path))
    logging.debug('However, I still have a lot to learn!')

if __name__ == '__main__':
    test_log()