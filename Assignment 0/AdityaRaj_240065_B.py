# -*- coding: utf-8 -*-
"""Copy of assgn1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DJNAYhIM8LAKQUugUWx7f1gmKjIdVkMF

# Simple application of essential python libraries

Get an intuitive and applicative understanding of numpy, pandas and matplotlib by using these libraries to play with data often found in real life applications.

This book is for understanding the libraries, so make sure to experiment as much as you can, you dont have to stick to exactly what is asked.

Guidelines:

*   Fill the codeblocks according to the comments given
*   Hints are given wherever required
*   Your first debugging step should be to print errors to identify the issue.Understand why it went wrong by analyzing the outputs and error messages. Adjust your code to fix the problem systematically.
*   If stuck, you're welcome to utilize any online resources, and feel free to ask doubts in the group!
"""

#import necessary dependencies
import urllib.request
# ...other dependencies

"""##Data to work on"""

# Step 1: Load the dataset, dont focus on this part
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
filename = "airtravel.csv"
urllib.request.urlretrieve(url, filename)

"""Where did this .csv file get saved? load it using pandas!"""

#load the .csv file using pandas
import pandas as pd
import numpy as np

df = pd.read_csv('airtravel.csv')
print(df)
#create an ndarray from this pandas df, but ignore the "Month" column (slicing, maybe?)
arr = np.array(df.iloc[:,1:4])
print(arr)

#Calculate the mean value across all three years for each month (mean_original) using an np function and return an ndarray consisting mean passengers for each month
def mean_pass(df):
  mean_pass = np.array([[1,2]])
  for i in range(len(df)):
    month = df.iloc[i,0]
    mean_original = df.iloc[i,1:4].mean()
    mean_pass = np.append(mean_pass, [[month, mean_original]], axis = 0)
  return mean_pass[1:]
(mean_pass(df))

#use matplotlib to plot a bargraph to visualize mean number of passengers across different months
import matplotlib.pyplot as plt

sorted_pairs = mean_pass(df)[mean_pass(df)[:, 1].argsort()]


x_value = sorted_pairs[:,0]
y_value = sorted_pairs[:,1]

plt.bar(x_value,y_value)
plt.title("Graph to show the mean number of passengers across different months.")
plt.xlabel("Month")
plt.ylabel("Mean number of passengers")
plt.show()

"""##Transforming data

Let's visualize the data

Simulate a spike across the data
"""

#Simply create a list with the same shape as previous arrays, and fill it with data simulating a spike across months peaking at 100, width, number of peaks, etc. are upto you!

spike = np.array([['JAN', 10], ['FEB', 20], ['MAR', 30], ['APR', 40], ['MAY', 50],
                  ['JUN', 60], ['JUL', 70], ['AUG', 80], ['SEP', 90], ['OCT', 100],
                  ['NOV', 15], ['DEC', 25]])
'''new_mean = np.array([])
for i in range(12):
  a = np.array([spike[i,0] ,float(spike[i,1]) + float(mean_pass(df)[i,1])])
  new_mean = np.append(new_mean, a, 0)'''

#convert the list to a pandas series spike_series, and the mean_original to a pandas series also
spike_series = pd.Series(spike[:,1], dtype = float)
mean_original = pd.Series(mean_pass(df)[:,1], dtype = float)

#define a function called transform_orig() that adds spike_series element-wise to original_series (use .add())
def transform_orig(a,b):
  return a.add(b)

#call the function and obtain a spiked_data series, and convert it back to a list
spiked_data = transform_orig(spike_series,mean_original)
new_data = np.array([[1,2]])
for i in range(12):
  new_data  = np.append(new_data,[[spike[i,0],spiked_data[i]]], axis = 0)
new_data = new_data[1:]

"""Plot the new spiked_data across months to visualize the spike's impact on number of passengers"""

#similar to how you plotted it before! (bonus: make it colorful)
sorted_pairs = new_data[new_data[:, 1].argsort()]


x_value = sorted_pairs[:,0]
y_value = sorted_pairs[:,1]
colors = ['#FF6347', '#3CB371', '#1E90FF', '#FFD700', '#8A2BE2']
plt.bar(x_value,y_value, color = colors)

plt.title("Graph to show the mean number of passengers across different months.")
plt.xlabel("Month")
plt.ylabel("Mean number of passengers along with the spike")
plt.show()

"""## Compare!

Now, all thats left is to compare the graphs
"""

#Create a subplot with first and second plot, along with a graph showing how the data has changed before and after spike (could be a bar graph, upto you, be creative)
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Plot 1: Bar graph of the original mean passengers
sorted_pairs_original = mean_pass(df)[mean_pass(df)[:, 1].argsort()]
x_value_original = sorted_pairs_original[:, 0]
y_value_original = sorted_pairs_original[:, 1]
axs[0].bar(x_value_original, y_value_original, color='blue', label='Original Data')
axs[0].set_title('Original Mean Passengers Across Different Months')
axs[0].set_xlabel('Month')
axs[0].set_ylabel('Mean Passengers')
axs[0].legend()

# Plot 2: Bar graph of the mean passengers after applying the spike (spiked data)
sorted_pairs_spiked = new_data[new_data[:, 1].argsort()]
x_value_spiked = sorted_pairs_spiked[:, 0]
y_value_spiked = sorted_pairs_spiked[:, 1]
axs[1].bar(x_value_spiked, y_value_spiked, color='green', label='Spiked Data')
axs[1].set_title('Mean Passengers with Spike')
axs[1].set_xlabel('Month')
axs[1].set_ylabel('Mean Passengers with Spike')
axs[1].legend()

# Plot 3: Bar graph showing the difference (change) between original and spiked data
change_in_data = spike[:,1]
axs[2].bar(x_value_original, change_in_data, color='orange', label='Change in Data')
axs[2].set_title('Difference Between Original and Spiked Data')
axs[2].set_xlabel('Month')
axs[2].set_ylabel('Difference in Passengers')
axs[2].legend()

plt.tight_layout()

plt.show()