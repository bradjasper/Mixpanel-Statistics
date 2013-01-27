# Mixpanel Statistics
A collection of Python scripts that pull API data from Mixpanel and 
perform statistics on the data. 

Currently supported:
    - Correlation Analysis
    - Regression Analysis


## Setup
Retrieve your API key and secret from Mixpanel API Information
(http://mixpanel.com/user/account/#info). Set the variables in your shell:

    export MIXPANEL_API_KEY=klsj234kljSLDKFJl243jlksdjf
    export MIXPANEL_API_SECRET=lkJSdlkj234lkjsdlfksjdflksjdf


## Correlation Analysis
Correlation determines the relationship between two variables. To 
determine the correlation of different Mixpanel events, do:

    ./correlation.py [event1] [event2] [event3]...
    ./correlation.py success_view checkout_view checkout_error
 

    Output
    ==============================================================================
    Correlation coefficients
    checkout_view	x	checkout_error:	0.600231
    checkout_view	x	success_view:	0.806892
    checkout_error	x	success_view:	0.469129
     

## Regression Analysis
Regression analysis studies the relationship between a dependent variable
and other independent variables. To perform regression analysis on your
Mixpanel events, do:

    ./regression.py [dependent_var] [independent_var1] [independent_var2]
    ./regression.py success_view checkout_view checkout_error

    Output
    ==============================================================================
    Dependent Variable: success_view
    Method: Least Squares
    Date:  Sun, 10 Jan 2010
    Time:  12:23:16
    # obs:                  60
    # variables:         3
    ==============================================================================
    variable     coefficient     std. Error      t-statistic     prob.
    ==============================================================================
    const           1.151644      0.767227      1.501047      0.138863
    checkout_view           0.049232      0.005862      8.398709      0.000000
    checkout_error          -0.032332      0.133101     -0.242911      0.808946
    ==============================================================================
    Models stats                         Residual stats
    ==============================================================================
    R-squared             0.651435         Durbin-Watson stat   2.219304
    Adjusted R-squared    0.639205         Omnibus stat         6.593467
    F-statistic           53.263875         Prob(Omnibus stat)   0.037004
    Prob (F-statistic)    0.000000         JB stat              5.678402
    Log likelihood       -160.875422         Prob(JB)             0.058472
    AIC criterion         5.462514         Skew                 0.649233
    BIC criterion         5.567231         Kurtosis             3.765081
    ==============================================================================
    Regression equation for response variable 'success_view'

    success_view = 1.15164371922 + 0.04923(checkout_view) + -0.03233(checkout_error)



## Contact
bjasper@gmail.com
