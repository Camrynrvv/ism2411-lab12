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

print("\nEXERCISE 3")

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)

    print("Header:")
    print(header)

    for row in reader:
        print(row)  

print("\nEXERCISE 4")

total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        revenue = price * quantity

        print(f"{product}: {quantity} units × ${price:.2f} = ${revenue:.2f}")

        total_revenue += revenue

print(f"\nTotal Revenue: ${total_revenue:.2f}")

print("\nEXERCISE 5")

original_rows = 0
written_rows = 0

with open("data/sales.csv", "r") as infile, open("data/cleaned.csv", "w", newline="") as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    next(reader)

    writer.writerow(["Product", "Price", "Qty", "Total"])

    for row in reader:
        original_rows += 1

        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity

        if total > 100:
            writer.writerow([product, price, quantity, f"{total:.2f}"])
            written_rows += 1

print(f"Rows written: {written_rows}")
print(f"Original rows: {original_rows}")

print("\nEXERCISE 6")

total_dict = 0

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])

        total_dict += price * quantity

print(f"Total Revenue Using DictReader: ${total_dict:.2f}")

# csv.reader uses column positions such as row[0] and row[1].
# DictReader uses column names, making the code easier to read and maintain.

print("\nEXERCISE 7")

summary = {}

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        revenue = price * quantity

        if product not in summary:
            summary[product] = 0

        summary[product] += revenue

for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

print("\nEXERCISE 8")

with open("data/run_log.txt", "a") as logfile:
    logfile.write(
        f"{datetime.now()} - Total Revenue: ${total_revenue:.2f}\n"
    )

print("Log entry added.")