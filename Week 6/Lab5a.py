import csv

def get_file(csv_file):
    with open(csv_file) as f:
        file = csv.reader(f)
        report = list(file)
        print(report)

ip_address = []

csv_file = str(input(r"Please enter a file path: "))
get_file(csv_file)