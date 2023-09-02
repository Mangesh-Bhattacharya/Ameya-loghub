import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
csv_file_path = 'Ameya-loghub-master/Ameya-loghub-master/Apache/Apache_2k.csv'
data = pd.read_csv(csv_file_path)

# Set up the figure with subplots
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Plot 1: Bar plot for Notice as Green and Error as red
ax1 = axes[0]
status_counts = data['Status'].value_counts()
ax1.bar(status_counts.index, status_counts.values, color=['green', 'red'])
ax1.set_xlabel('Status')
ax1.set_ylabel('Count')
ax1.set_title('Apache Log Classification')

# Plot 2: Pie chart - HH:mm:ss as green and Status as red
ax2 = axes[1]
ax2.pie(status_counts.values, labels=status_counts.index, autopct='%1.1f%%',
    colors=['green', 'red'])
ax2.set_title('Apache Log Classification')
plt.tight_layout(); #**Question:** What is your takeaway from this visualization? **Answer**: The pie charts shows that most of the logs are related to error

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()
