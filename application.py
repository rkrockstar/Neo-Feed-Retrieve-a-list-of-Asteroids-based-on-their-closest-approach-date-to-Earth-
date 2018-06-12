#import urllib
import json
from urllib.request import urlopen
#import requests
from datetime import datetime
import sys

#This function takes the valid input and exits the application if the input is invalid

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

#This function gets the data from the NASA API and returns it in string format
def get_url(g, h):
    api_url = 'https://api.nasa.gov/neo/rest/v1/feed?'
    api_key = '&api_key=DEMO_KEY'
    locality = 'start_date=' + g + '&' + 'end_date=' + h
    final_url = api_url + locality + api_key        #This is the final url with the start and end dates and the Demo key
    json_obj = urlopen(final_url)
    data = json.load(json_obj)
    return data             #Data is returned in string format


m = {} #Dictionary used for retriving minimum Epoch data for close approach to earth for an Asteroid

#This function sorts the data based on the miles per hour relative velocity of each year.

def summary_with_sorting(a):

    for i in a:
        s = str(i)
        c = {}
        print("Asteroids for the year: {}".format(s)) #Data is sorted as per the year
        for k in range(len(a[s])-1):
            neo_id = a[s][k]["neo_reference_id"]   #Every asteroid has a unique neo_reference_id
            velocity = a[s][k]["close_approach_data"][0]["relative_velocity"]["miles_per_hour"]    #Every asteroid's relative velocity in miles_per_hour

            c.update({neo_id:velocity}) #Dictionary containing neo_id and relative velocities

        ddd = sorted(c, key=c.__getitem__) #The dictionary is sorted as per the values which are relative velocities and the keys, which are neo_id, are returned

        print("Summary of resulting data sorted ascending by velocity:")
        for h in ddd:
            for k in range(len(a[s]) - 1):
                if a[s][k]["neo_reference_id"] == h:
                    fd = a[s][k]
            for k, v in fd.items():    #The output is printed as Key : Value pairs, This is a human readable format
                print(k, v)
            #print(fd)


def asteroid_closest_proximity(b):
    for j in b:
        s = str(j)
        for k in range(len(b[s]) - 1):
            ff = b[s][k]["name"]        #Asteroid names
            f = b[j][k]["close_approach_data"][0]["epoch_date_close_approach"]   #Epoch data for close approach to earth for an Asteroid
            m.update({ff: f})

    ss = min(m, key=m.get) #Key of the minimum value, which is close approach, is returned
    print("***********************************************************************")
    print("Name of the asteroid with closest proximity in all Asteroids:")
    print(ss)



def main():

    a, b = input_dates()
    d = get_url(a, b)      #Input dates are passed to get the data from NASA API
    summary_with_sorting(d["near_earth_objects"])  #Only the near_earth_objects data is passed and the sorted summary of the data is retrived by relative velocity
    asteroid_closest_proximity(d["near_earth_objects"])   #The asteroid with closest proximity is determined based on Close_Approch_data

main()



