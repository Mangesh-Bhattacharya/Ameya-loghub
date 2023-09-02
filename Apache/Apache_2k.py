#
#
########################################################################
#
#
###### Ameya Cloud Solutions - Booster Pack Project ######
###### CEO Ganesan Vertiselvan
###### Proj. Mgr. Pankaj Sharma ######
###### DS-Int. Mangesh Bhattachayra ######
#
#
########################################################################
# Preprocessing Python programme to read and analyze the Apache_2k.log file

import re
import csv

# Function to extract components from log entry

def extract_components(line):
    match = re.search(
        r'(\w{3}) (\d{1,2}) (\d{2}:\d{2}:\d{2}) (\d{4}).*?(notice|error|ok)', line)
    month, day, time, year, status = match.groups()
    return month, day, time, year, status


# Read the .log file and process lines
log_file_path = 'Ameya-loghub-master/Ameya-loghub-master/Apache/Apache_2k.log'
csv_file_path = 'Ameya-loghub-master/Ameya-loghub-master/Apache/Apache_2k.csv'

with open(log_file_path, 'r') as log_file:
    log_lines = log_file.readlines()

preprocessed_data = []

for line in log_lines:
    day, month, time, year, status = extract_components(line)
    preprocessed_data.append((day, month, time, year, status))

# Write preprocessed data to a CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header
    csv_writer.writerow(['Month', 'Day', 'HH:mm:ss', 'Year', 'Status'])

    for row in preprocessed_data:
        csv_writer.writerow(row)

print(f'Log file {log_file_path} has been preprocessed and saved as {csv_file_path}')
