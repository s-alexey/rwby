from lxml import html
import requests
import datetime
from .utils import to_datetime

DATE_FORMAT = '%Y-%m-%d'
SEARCH_URL = 'http://rasp.rw.by/m/{lang}/route/'

value2xpath = {
    'from': 'div/div/span[@class="about_from"]/text()',
    'to': 'div/div/span[@class="about_to"]/text()',
    # 'date_verbose': 'div/small[@class="about_date"]/text()',
    'train_id': 'div/div/small[@class="train_id"]/text()',
    'train_title': 'div/div[@class="train_title"]/text()[2]',
    'train_type': 'div/div[@class="train_type"]/text()[2]',
    'departure_time': 'div/div[@class="route_start"]/div[@class="route_time"]/text()',
    'arrival_time': 'div/div[@class="route_end"]/div[@class="route_time"]/text()',
}

place2xpath = {
    'type': 'td[@class="places_name"]/text()',
    'price': 'td[@class="places_price"]/span[@class="denom_after"]/text()',
    'quantity': 'td[@class="places_qty"]/text()',
}


def train_info(train, date):
    data = {
        v: train.xpath(p)[0].strip().replace('\xa0', ' ')
        for v, p in value2xpath.items()
    }
    places = train.xpath('*/*[@class="places_table"]/tr')
    data['places'] = [
        {v: place.xpath(p)[0].strip() for v, p in place2xpath.items()}
        for place in places
    ]
    data['arrival_time'] = to_datetime(data['arrival_time'], date)
    data['departure_time'] = to_datetime(data['departure_time'], date)

    return data


def trains(tree, date):
    return [train_info(train, date) for train in tree.xpath("//div[contains(@class, 'train_details')]")]


def search(from_station, to_station, date, lang='ru', **kwargs):
    """ Search the API for trains. """

    if isinstance(date, datetime.date):
        date = date.strftime(DATE_FORMAT)

    kwargs['from'] = from_station
    kwargs['to'] = to_station
    kwargs['date'] = date
    kwargs['s'] = 'mobile'

    response = requests.get(SEARCH_URL.format(lang=lang), params=kwargs)

    tree = html.fromstring(response.content)
    return trains(tree, datetime.datetime.strptime(date, DATE_FORMAT))
