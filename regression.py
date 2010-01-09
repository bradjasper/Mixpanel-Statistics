import ols
from numpy.random import randn
from numpy import ndarray, array

data = randn(100, 6)
y = data[:,0]
x = data[:,1:]

"""
y = array([1, 2, 3, 4, 5, 6])
x = array([
            array([1, 2, 3, 4, 5]),
            array([1, 2, 3, 4, 5]),
            array([1, 2, 3, 4, 5]),
            array([1, 2, 3, 4, 5]),
            array([1, 2, 3, 4, 5]),
            array([1, 2, 3, 4, 5]),
          ])
          """



final_list = []

for z in x:
    tmp_list = []
    for r in z:
        tmp_list.append(float(r))
    final_list.append(array(tmp_list))
    tmp_list = []
final_list = array(final_list)

print final_list

#jprint x
#print final_list

#assert False, (len(x), len(final_list), type(x), type(final_list))
#x = array(final_list)
#x = array([z for z in x[:15]])

print y
print x

print len(x), len(y)

mymodel = ols.ols(y, x, 'y1', ['x1', 'x2', 'x3', 'x4', 'x5'])

print mymodel.p

mymodel.summary()


"""
from itertools import chain
import os
from sets import ImmutableSet
import pprint

from numpy import array
from statlib.stats import apearsonr

from mixpanel import Mixpanel

NUM_DAYS = 999
events = ['success_view', 'checkout_view', 'checkout_error', '500_error',
        'search_error', 'status_view', 'cancel_view', 'results_expire',
        'results_none_active', 'results_none_finished']

client = Mixpanel(api_key=os.environ['MIXPANEL_API_KEY'], api_secret=os.environ["MIXPANEL_API_SECRET"])

print "Collecting data from MixPanel"

data = client.request('events', 'general', {
    'event' : events,
    'unit' : 'day',
    'interval' : NUM_DAYS,
})

series = data["data"]["values"]

dates = set(chain(*[value.keys() for key, value in series.iteritems()]))
sorted(dates)

event_data = {}

# Normalize event data
for date in dates:
    for name in series:
        val = series[name].get(date, 0)
        try:
            event_data[name].append(val)
        except KeyError:
            event_data[name] = [val]


# Convert event data to numpy arrays
for event, data in event_data.iteritems():
    event_data[event] = array(data)


# Generate Event Pairs
event_pairs = set()
for event in event_data:
    for event2 in event_data:
        if event != event2:
            event_pairs.add(ImmutableSet([event, event2]))

print "Correlation statistics for %s" % events

for event1, event2 in event_pairs:

    rval, pval = apearsonr(event_data[event1], event_data[event2])

    if rval > .5:
        print "Correlation between %s and %s: %f" % (event1, event2, rval)
        print "P-value: %.10f" % pval
        print
"""
