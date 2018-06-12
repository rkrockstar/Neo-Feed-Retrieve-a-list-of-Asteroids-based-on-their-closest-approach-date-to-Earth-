import urllib
import json
from urllib.request import urlopen
import requests
from datetime import datetime
import sys

def input_dates():
    print("Input Start Date:")
    starting_date = input()
    sd = datetime.strptime(starting_date , '%Y-%m-%d')
    print("Input End Date:")
    ending_date = input()
    ed = datetime.strptime(ending_date, '%Y-%m-%d')
    if ed < sd:
        print('End date is less than Start Date. Please check the input.')
        sys.exit()
    else:
        return starting_date, ending_date


# demo key    https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY

def get_url(g, h):
    api_url = 'https://api.nasa.gov/neo/rest/v1/feed?'
    api_key = '&api_key=DEMO_KEY'
    locality = 'start_date=' + g + '&' + 'end_date=' + h
    final_url = api_url + locality + api_key
    json_obj = urlopen(final_url)
    data = json.load(json_obj)
    return data


m = {}
def summary_with_sorting(a):

    for i in a:
        s = str(i)
        c = {}
        print("Asteroids for the year: {}".format(s))
        for k in range(len(a[s])-1):
            neo_id = a[s][k]["neo_reference_id"]
            velocity = a[s][k]["close_approach_data"][0]["relative_velocity"]["miles_per_hour"]

            c.update({neo_id:velocity})

        ddd = sorted(c, key=c.__getitem__)

        print("Summary of resulting data sorted ascending by velocity:")
        for h in ddd:
            for k in range(len(a[s]) - 1):
                if a[s][k]["neo_reference_id"] == h:
                    fd = a[s][k]
            for k, v in fd.items():
                print(k, v)
            #print(fd)


def asteroid_closest_proximity(b):
    for j in b:
        s = str(j)
        for k in range(len(b[s]) - 1):
            ff = b[s][k]["name"]
            f = b[j][k]["close_approach_data"][0]["epoch_date_close_approach"]
            m.update({ff: f})

    ss = min(m, key=m.get)
    print("***********************************************************************")
    print("Name of the asteroid with closest proximity in all Asteroids:")
    print(ss)



def main():

    a, b = input_dates()
    d = get_url(a, b)
    print(d["near_earth_objects"])
    summary_with_sorting(d["near_earth_objects"])
    asteroid_closest_proximity(d["near_earth_objects"])

main()



