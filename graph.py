"""
Data Visualization Project

Parse data from an ugly CSV or Excel file, and render it in
JSON-like form, visualize in graphs, and plot on Google Maps.

Part II: Take the data we just parsed and visualize it using popular
Python math libraries.
"""

from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np


MY_FILE = "sample_sfpd_incident_all.csv"


def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-like object"""

    # Open CSV file, and safely close it when we're done
    opened_file = open(raw_file)

    # Read the CSV data
    csv_data = csv.reader(opened_file, delimiter=delimiter)

    # Setup an empty list
    parsed_data = []

    # Skip over the first line of the file for the headers
    fields = csv_data.next()

    # Iterate over each row of the csv file, zip together field -> value
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    # Close the CSV file
    opened_file.close()

    return parsed_data


def visualize_days():
    """Visualize data by day of week"""

    # grab our parsed data that we parsed earlier
    data_file = parse(MY_FILE, ',')

    # make a new variable, 'counter' from iterating through each
    # line of data in the parsed data, and count how many incidents
    # happen on each day of the week
    counter = Counter(item["DayOfWeek"] for item in data_file)

    # seperate the x-axis data (the days of the week from the 
    # 'counter' variable from the y-axis data (the number of 
    # incidents for each day)

    data_list = [
                  counter["Monday"],
                  counter["Tuesday"],
                  counter["Wednesday"],
                  counter["Thursday"],
                  counter["Friday"],
                  counter["Saturday"],
                  counter["Sunday"]
    ]

    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    # with that y-axis data, assign it to a matplot lib plot instance
    plt.plot(data_list)
    
    # create the amount of ticks needed for our x-axis, and assign
    # the lables
    plt.xticks(range(len(day_tuple)), day_tuple)

    # save the graph
    plt.savefig("Days.png")

    # close figure
    plt.clf()

def visualize_type():
    """Visualize data by category in a bar graph"""

    # grab our parsed data
    data_file = parse(MY_FILE, ",")

    # make a new variable counter, by iterating through the parsed data
    # counting number on instances by category 
    counter = Counter(item["Category"] for item in data_file)

    # set the labels which are based on the keys of our counter.
    # since order doesn't matter, we can just use counter.keys()
    labels = tuple(counter.keys())

    # set exactly where the labels hit the x-axis
    xlocations = np.arange(len(labels)) + 0.5

    # width of each bar that will be plotted
    width = 0.5

    # assign data to a bar plot (similar to plt.plot()!)
    plt.bar(xlocations, counter.values(), width=width)

    # assign graph title
    plt.title("Crime by Category: San Franciso 2003")

    # assign y-axis label
    plt.ylabel("Count")

    # assign x-axis label
    plt.xlabel("Category")

    # assign labels and tick location to x-axis
    plt.xticks(xlocations + width/2, labels, rotation=90)

    # give some more room so the x-axis labels aren't cut off in graph
    plt.subplots_adjust(bottom=0.4)

    # make overall graph larger
    plt.rcParams['figure.figsize'] = 12, 8

    # save the graph
    plt.savefig("Type.png")
    
    # display the graph
    #plt.show()

    # close plot figure
    plt.clf()


def main():
    visualize_days()
    visualize_type()

if __name__ == "__main__":
    main()        
