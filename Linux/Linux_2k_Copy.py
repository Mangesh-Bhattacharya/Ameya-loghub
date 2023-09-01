#
#
########################################################################
#
#
###### Mangesh Bhattachayra ######
###### Ameya Cloud Solutions - Booster Pack Project ######
#
#
########################################################################
# Build a preprocessing python code that reads a .log file

import re
import csv

# Function to extract components from log entry

def extract_components(line):
    auth_failure_match = re.search(r'authentication failure', line)
    date_match = re.search(r'^\w{3} \d{1,2}', line)
    time_match = re.search(r'\d{2}:\d{2}:\d{2}', line)
    year_match = re.search(r'\d{4}', line)
    rhost_match = re.search(r'rhost=.*? ', line)
    packages_match = re.search(
        r'packages (sshd|su|ftpd|snmpd|klogind|gdm|xinetd|syslogd)', line)

    auth_failure = 'authentication failure' if auth_failure_match else ''
    date = date_match.group() if date_match else ''
    time = time_match.group() if time_match else ''
    year = year_match.group() if year_match else ''
    rhost = rhost_match.group() if rhost_match else ''
    packages = packages_match.group(1) if packages_match else ''

    return auth_failure, date, time, year, rhost, packages


# Read the .log file and process lines
log_file_path = 'Linux/Linux_2k_Copy.log'
csv_file_path = 'Linux/Linux_2k_Copy.csv'

with open(log_file_path, 'r') as log_file:
    log_lines = log_file.readlines()

preprocessed_data = []

for line in log_lines:
    auth_failure, date, time, year, rhost, packages = extract_components(line)
    preprocessed_data.append((auth_failure, date, time, year, rhost, packages))

# Write preprocessed data to a CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header
    csv_writer.writerow(['Authentication Failure', 'Month-Date',
                        'HH:mm:ss', 'Year', 'rhost', 'Packages'])

    for row in preprocessed_data:
        csv_writer.writerow(row)

print(f'Log file {log_file_path} has been preprocessed and saved as {csv_file_path}')
