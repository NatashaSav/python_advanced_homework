from datetime import date

from decorator_h_w.third_task.application.db import people
from decorator_h_w.third_task.application import salary

if __name__ == '__main__':
    people.get_employees()
    salary.calculate_salary(25, 5)
    print(date.today())


