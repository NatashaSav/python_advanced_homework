import logging

FORMAT = "%(asctime)s %(funcName)s():%(levelname)s: %(message)s"
logging.basicConfig(filename='./third_task.log', filemode='w', format=FORMAT, level=logging.INFO)
result = logging.Formatter(FORMAT)
logger = logging.getLogger(__name__)


def decorator(func):
    def wrap_log(*args, **kwargs):
        name = func.__name__
        logger = logging.getLogger(name)
        result = func(*args, **kwargs)
        logger.info("Имя функции %s Все аргументы  %s %s  Результат: %s", name, *args, result)
        return func

    return wrap_log

@decorator
def calculate_salary(a, b):
    print("Salary info")
    return a * b