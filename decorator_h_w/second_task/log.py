import logging
import functools


def _generate_log(path):
    logger = logging.getLogger('LogError')
    logger.setLevel(logging.ERROR)
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(path)

    log_format = "%(asctime)s %(funcName)s():%(levelname)s: %(message)s"
    formatter = logging.Formatter(log_format)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger


def log_error(path='log.error.log'):

    def error_log(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger = _generate_log(path)
                error_msg = 'Error has occurred'
                logger.exception(error_msg)
                logger.info("Все аргументы  %s %s", *args)
                return e

        return wrapper

    return error_log
