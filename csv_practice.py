# Reflection Question 1:
# Python makes ETL tasks easier because it can automatically read,
# transform, and write large amounts of data with little manual effort.
# Excel is easier for quick visual analysis, while Python is better
# for automation and repetitive processing.

# Reflection Question 2:
# A sales reporting system would benefit from an append-mode log file.
# Each time a report runs, a new entry can be added without removing
# previous records, creating a useful audit trail.

import csv
from datetime import datetime

print("EXERCISE 2")

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)