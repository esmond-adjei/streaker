from datetime import date, timedelta
import math


def roundn(number: float) -> int:
    int_num = int(number)
    return math.ceil(number) if (number - int_num) >= 0.5 else math.floor(number)


def getEndDate(start_date: str, days_per_week: int, completion_period: int ) -> date:
    """Calculates the time date by which an event will be due
    given the number of times it is performed in a week [days_per_week]
    and the total number of times to perform the action [completion_period]
    
    - params: start_date - start date of the event eg: 2024-01-24 -> Jan 24, 2024
              days_per_week - number of times event is performed in a week
              completion_period - total number of times event to completion of event
    - Return: Date in string format
    """
    if not isinstance(completion_period, int):
        return date(2069, 1, 1)
    if not isinstance(start_date, date):
        sdate = [int(d) for d in start_date.split('-')]
        sdate = date(*sdate)
    else:
        sdate = start_date
    return sdate + timedelta(roundn((completion_period/days_per_week) * 7 - 1))


if __name__ == '__main__':
    start_date = '2024-01-09'
    days_per_week = 3
    completion_period = 6
    end_date = getEndDate(start_date, days_per_week, completion_period)
    print(end_date) # -> 2024-01-22
    
    print(roundn(2.5)) # -> 3
    print(roundn(2.9)) # -> 3
    print(roundn(2.1)) # -> 2