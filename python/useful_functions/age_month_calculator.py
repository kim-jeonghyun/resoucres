from dateutil.relativedelta import relativedelta
from datetime import datetime
import numpy as np


def get_age_month_1(start, end):
    """
    2개의 str 타입 날짜를 받으면, dateutil.relativedelta library를 활용해 월령을 반환
    """

    try:
        start_date =  datetime.strptime(start,'%Y-%m-%d').date()
        end_date =  datetime.strptime(end,'%Y-%m-%d').date()
        delta = relativedelta(end_date, start_date)  # 두 날짜의 차이 구하기
        result = 12 * delta.years + delta.months  # 두 날짜의 차이나는 개월수
        return result
    except:
        return np.nan

def get_age_month_2(start, end):
    """
    2개의 str 타입 날짜를 받으면, 날짜의 차이를 30으로 나눠서 월령을 구하여 반환
    """
    try:
        start_date =  datetime.strptime(start,'%Y-%m-%d').date()
        end_date =  datetime.strptime(end,'%Y-%m-%d').date()
        diff = (end_date-start_date).days/30
        return round(diff,0)
    except:
        return np.nan