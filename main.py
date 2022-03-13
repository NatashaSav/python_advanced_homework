from application.db import people
from application import salary
from datetime import date


if __name__ == '__main__':
    people.get_employees()
    salary.calculate_salary()
    print(date.today())


