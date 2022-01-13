"""
Read the data from the csv file for student availability.
@author: Zoe Bingham
"""

import csv
import re
from graph_settings import *

def read_availability(filename=FILENAME, point_system=POINTS):
    """
    Returns a days and times dictionary od dictionaries with point system
    """
    # Prepare file to be processed
    with open(filename) as file:
        reader = csv.reader(file)
        columns = dict()    # Keeps track of the indices and labels
        likliehood_index = -1   # Index for liklieness of attendance
        week_dict = init_week_dict()    # Initializes with scores of 0 for all times
        count = 0
        # Break the records up into a dictionary with the key of how likely a student is to attend a session and the times that the student is available.
        for line in reader:
            # Keep track of the order in which the data is separated
            if count == 0:
                index = 0
                for record in line:
                    for time in TIMES:
                        # Record the index of the likliehood of attendance in the columns dictionary
                        if re.search('attend', record):
                            columns[index] = 'Likliehood'
                            likliehood_index = index
                        # Record the index of the time in the columns dictionary
                        if re.search(('%s'%time),record):
                            columns[index] = time
                    index += 1
                count += 1
            else:
                for index in columns:
                    # Process all the times
                    if line[index] != line[likliehood_index]:
                        time = columns[index]
                        days = line[index]
                        #print(time + ": " + days)   
                        tokens = days.split(", ")
                        for day in tokens:
                            likliehood = line[likliehood_index]
                            #print(day + " " + likliehood)
                            if day != '':
                                week_dict[day][time] += point_system[likliehood]
                                #print(week_dict[day][time])
                #print()               
        #print(columns)
    return week_dict

def init_week_dict():
    """
    Fills all times with a score of 0
    """
    week_dict = dict()
    for day in DAYS:
        day_dict = dict()
        for time in TIMES:
            day_dict[time] = 0
        week_dict[day] = day_dict
    return week_dict

#print(init_week_dict())

def main():
    print(read_availability(FILENAME, POINTS))

if __name__ == "__main__":
    main()