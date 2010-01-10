"""Utilities for working with Mixpanel stats"""

import os
from itertools import chain
from sets import ImmutableSet

from numpy import array

from mixpanel import Mixpanel

DEFAULT_UNIT = "day"
DEFAULT_INTERVAL = 60

def get_event_data(events, unit=DEFAULT_UNIT, interval=DEFAULT_INTERVAL):
    """Retrieve event data for a list of events"""

    MIXPANEL_API_KEY = os.environ["MIXPANEL_API_KEY"]
    MIXPANEL_API_SECRET = os.environ["MIXPANEL_API_SECRET"]

    client = Mixpanel(api_key=MIXPANEL_API_KEY, api_secret=MIXPANEL_API_SECRET)

    response = client.request('events', 'general', {
        'event' : events,
        'unit' : unit,
        'interval' : interval
    })

    return response['data']['values']


def event_data_to_matrix(series, events):
    """Given a dictionary of event/data, normalize the data into a matrix"""

    # Get all dates from this series
    all_dates = set(chain(*[value.keys() for key, value in series.iteritems()]))
    sorted(all_dates)

    normalized = []

    for date in all_dates:
        row = []
        for event in events:
            try:
                row.append(series[event].get(date, 0))
            except KeyError:
                raise ValueError("Unable to find event '%s' in response data from Mixpanel" % event)
        normalized.append(array(row))
    return array(normalized)


def list_to_pairs(items):
    """Given a list of items, return a list of unique pairs"""
    # Generate Event Pairs
    item_pairs = set()
    for item in items:
        for item2 in items:
            if item != item2:
                item_pairs.add(ImmutableSet([item, item2]))
    return item_pairs
