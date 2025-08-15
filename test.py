# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:01:14 2024

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Load the Excel file
df = pd.read_excel('under_eller_over_dl.xlsx', sheet_name='Pb',header=[0, 1])


# Initialize the plot
plt.figure()
plt.title('Pb', fontsize=15)
plt.ylabel('[$\mu$g/L]', fontsize=13)
#plt.grid()

labels = [f"{col[0]}\n{col[1]}" for col in df.columns]


# Prepare the data as a list of columns for boxplot
data = [df[column].dropna() for column in df.columns]  # Drop any NaNs to avoid errors

# Generate the boxplot with patch_artist=True to enable color fill
boxplot = plt.boxplot(data, patch_artist=True, labels=labels,widths=0.2)

# Define colors for each box (adjust as needed to match the number of columns)
colors = ['#fdef90', '#9996ff','#f895d9','#acff9b', '#90e0ef',  '#f4a261', '#FF6F61']



# Apply colors to each box
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

for median in boxplot['medians']:
    median.set_color('black')


# === Add annotations ===
# Note: All boxplot elements are lists of line objects; index [0] corresponds to the first box

# Get the x position (center of box)
x = 1  # only one boxplot, so x=1

# Whiskers
whisker_lines = boxplot['whiskers']
lower_whisker_y = whisker_lines[0].get_ydata()[1]
upper_whisker_y = whisker_lines[1].get_ydata()[1]


values = data[0].sort_values()
Q1 = np.percentile(values, 25)
Q3 = np.percentile(values, 75)
median_val = np.median(values)



# Save and display the plot
#plt.savefig("F_Pb2.png", dpi=300)
plt.show()