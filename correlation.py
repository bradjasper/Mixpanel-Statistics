#!/usr/bin/env python

import sys

from scipy import corrcoef

from utils import get_event_data, event_data_to_matrix, list_to_pairs

def main(events):

    data = get_event_data(events)
    matrix = event_data_to_matrix(data, events)

    print "Correlation coefficients"

    for event1, event2 in list_to_pairs(events):

        data1 = matrix[:,events.index(event1)]
        data2 = matrix[:,events.index(event2)]

        coeff = corrcoef(data1, data2)[0][1]

        print "%s\tx\t%s:\t%f" % (event1, event2, coeff)



if __name__ == "__main__":

    if len(sys.argv) < 3:
        sys.exit("ERROR: Please enter at least 2 events to perform correlation" \
            + "analysis. Like this: './correlation.py event_1 event_2")

    main(sys.argv[1::])
