#!/usr/bin/env python

import sys

from ols import ols

from utils import get_event_data, event_data_to_matrix

def main(events):

    data = get_event_data(events)

    if len(data) == 0:
        sys.exit("ERROR: Unable to retrieve data from Mixpanel")

    matrix = event_data_to_matrix(data, events)

    response_name = events.pop(0)
    response_data = matrix[:,0]

    predictors_data = matrix[:,1:]
    predictors_names = events

    model = ols(response_data, predictors_data, response_name, predictors_names)

    model.summary()

    ## Generate Equation

    # Gather list of coefficients so we can build our formula
    coeff_dict = dict(zip(model.x_varnm, model.b))

    equation = "%s = %s" % (response_name, coeff_dict['const']) # Start with constant coefficient

    for name in predictors_names:
        val = coeff_dict[name]
        equation += " + %.5f(%s)" % (val, name)

    print "Regression equation for response variable '%s'" % response_name
    print
    print equation

if __name__ == "__main__":

    if len(sys.argv) < 3:
        sys.exit("ERROR: Please enter at least 1 predictor and 1 response event " \
            + "to analyse. Like this: './regression.py predictor_event " \
            + "response_event1 response_event2'")

    main(sys.argv[1::])
