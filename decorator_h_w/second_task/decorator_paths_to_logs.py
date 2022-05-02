import log

@log.log_error()
def divide(num1, num2):
    return num1 / num2

if __name__ == '__main__':
    result = divide(10, 0)
    print(result)
