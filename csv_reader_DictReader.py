import csv

# Utilisation de csv.reader
with open("example.csv", "r") as file:
    reader = csv.reader(file)
    list_of_lists = [row for row in reader]

print("csv.reader output:")
print(list_of_lists)

# Utilisation de csv.DictReader
with open("example.csv", "r") as file:
    dict_reader = csv.DictReader(file)
    list_of_dicts = [row for row in dict_reader]

print("\ncsv.DictReader output:")
print(list_of_dicts)
