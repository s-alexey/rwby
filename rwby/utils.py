import datetime
import re


def date2dict(d):
    return dict(month=d.month, day=d.day, year=d.year)


def to_datetime(time, default_date):
    result = re.match(r'(?P<hour>\d\d):(?P<minute>\d\d)(,\s+(?P<day>\d\d)\s+\w+)?', time).groupdict()

    date = date2dict(default_date)

    if result['day']:
        # NOTE: Assume that trip cannot last more than a month.
        if int(result['day']) < default_date.day:
            date['month'] += 1
            if date['month'] == 13:
                date['month'] = 1
                date['year'] += 1
            date.pop('day')
    result.update(date)

    return datetime.datetime(**{k: int(v) for k, v in result.items()})


