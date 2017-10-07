#!/usr/local/bin/python3

import pandas as pd

# series_minute = pd.Series([1, 2, 3], pd.DatetimeIndex([
# 	'2011-12-31 23:59:00',
# 	'2012-01-01 00:00:00',
# 	'2012-01-01 00:02:00']))

# print(series_minute.index.resolution) #minutes

# print(series_minute['2012'])
# print(series_minute['2011'])

periods = 12
date_range = pd.Series([x for x in range(1, periods+1, 1)], pd.DatetimeIndex(pd.date_range(start = pd.datetime(2017, 1, 1), periods = periods, freq='m')))
print('Date range resolution:', date_range.index.resolution, '\n\n') #day

print('All 2017 dates:\n', date_range['2017'], '\n\n')
print('All days in October:\n', date_range['2017-10'], '\n\n')
print('All day 31 of  October 2017: ', date_range['2017-10-31'])
