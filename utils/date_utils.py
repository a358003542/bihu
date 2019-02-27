#!/usr/bin/env python
# -*-coding:utf-8-*-

from datetime import datetime

from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrule, MONTHLY


def is_same_year(dt1, dt2):
    if (dt1.year == dt2.year):
        return True
    else:
        return False


def is_same_month(dt1, dt2):
    if (dt1.year == dt2.year) and (dt1.month == dt2.month):
        return True
    else:
        return False


def is_same_day(dt1, dt2):
    if (dt1.year == dt2.year) and (dt1.month == dt2.month) and (dt1.day == dt2.day):
        return True
    else:
        return False


def is_same_hour(dt1, dt2):
    if (dt1.year == dt2.year) and (dt1.month == dt2.month) and (dt1.day == dt2.day) and (dt1.hour == dt2.hour):
        return True
    else:
        return False


def round_to_day(dt):
    res = dt.replace(hour=0, minute=0, second=0, microsecond=0)
    return res


def round_to_hour(dt):
    res = dt.replace(minute=0, second=0, microsecond=0)
    return res


def round_to_minute(dt):
    res = dt.replace(second=0, microsecond=0)
    return res


def round_to_second(dt):
    res = dt.replace(microsecond=0)
    return res


def get_date_range(months):
    """
    返回一个时间片列表，以当前时间为终点，向前数几个月
    :param months:
    :return:
    """
    now = datetime.utcnow()
    sdt = now - relativedelta(months=months)
    return list(rrule(freq=MONTHLY, dtstart=sdt, until=now))


utcnow = datetime.utcnow()
one_week_ago = datetime.utcnow() - relativedelta(weeks=1)
one_day_ago = datetime.utcnow() - relativedelta(days=1)
two_day_ago = datetime.utcnow() - relativedelta(days=2)
one_hour_ago = datetime.utcnow() - relativedelta(hours=1)
one_month_ago = datetime.utcnow() - relativedelta(months=1)

__all__ = [
    'utcnow',
    'one_week_ago',
    'one_day_ago',
    'two_day_ago',
    'one_hour_ago',
    'one_month_ago'
]
