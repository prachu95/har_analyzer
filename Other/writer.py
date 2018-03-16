import csv

# "a" -> Appends the data onto to the created CSV file.
with open ("csv_test.csv", "a") as csv_file:
    csv_app = csv.writer(csv_file)
    csv_app.writerow(["V",
                      "Prashanth",
                      "Tirupachur",
                      9884615644])
#csv_app.writerow(["ef", "Pradfefe", "efvee", 4353536])
#csv_app.writerow(["fewfer", "fvvefvr", "htmwghtt", 943535454354])
