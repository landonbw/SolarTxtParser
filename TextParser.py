import pandas as pa
import numpy as np
import re

def GetHeadandTable(file):
    header_text = pa.read_table(file, sep='\s+', nrows=1, header=None)
    text_table = pa.read_table(file, sep='\s+', skiprows=2)
    return header_text, text_table

def AppendYears(body):
    year = 1990
    years = []

    for month in body['MO']:
        if year > 1990:
            years.append(year)
        else:
            years.append('avg')

        if int(month) > 20:
            year += 1

    body[year] = years
    return body

def DeleteSillyRows(body):
    # body = body[body.FL != np.nan]
    body = body[pa.notnull(body['FL'])]
    return body

def AddLatLon(body, head):
    # find lat
    head = head.transpose()
    lat = ''
    lon = ''
    for row in head[0]:
        if re.search(re.compile('^[NS][0-9][0-9]'), str(row)):
            lat += row
        if re.search(re.compile('^[EW][0-9][0-9]'), str(row)):
            lon += row
    # find lon
    # find location name
    # add values to body
    return 0


if __name__ == "__main__":
    filename = "/Users/landonwright/Documents/Code/SolarTxtParser/dailyStats/NSRDB_DailyStatistics_19910101_20101231_700260.txt"
    head, body = GetHeadandTable(filename)
    body = AppendYears(body)
    body = DeleteSillyRows(body)
    body = AddLatLon(body, head)
    print('done')

