# First,import some Python libraries.
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
# Change the working directory to where the full_data.csv file is stored.
os.chdir("C:/cygwin64/home/lenovo/practical7")
covid_data = pd.read_csv("full_data(2).csv")
covid_data.info()
# The code for showing the first and third columns from rows 10-20 (inclusive).
print(covid_data.iloc[10:20, [ 1, 3]])
n = 0
while n<7996:# According to the info. command, the file contains 7,996 lines.
        if covid_data.loc[n, "location"] == "Afghanistan": # Filter the row whose title is Afghanistan.
            covid_data.loc[n, "location"] = True
        else:
            covid_data.loc[n, "location"] = False
        Rows = list(covid_data.loc[:, "location"]) # Create and print a list containing the previously printed True/False.
        n+=1
print(covid_data.loc[Rows, "total_cases"])

import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
# Change the working directory to where the full_data.csv file is stored.
os.chdir("C:/cygwin64/home/lenovo/practical7")
covid_data = pd.read_csv("full_data(2).csv")
a = 0
my_columns = [True, False, True, True, False, False]# I used Boolean variables to determine which columns I wanted in my table
china_new_data = []
while a<7996:
        if covid_data.loc[a, "location"] == "China":
            covid_data.loc[a, "location"] = True
        else:
            covid_data.loc[a, "location"] = False # Filter the row whose title is China
        Rows2 = list(covid_data.loc[:, "location"]) # The above steps are basically the same as those in Afghanistan.
        a+=1
china_new_data = covid_data.loc[Rows2, my_columns]
print(china_new_data)
print(china_new_data.mean())# Here,I use the command (mean) to calculate the average.
# The mean of new cases = 893.923913.The mean of new deaths = 35.967391.
b = china_new_data.loc[:, ['new_cases', 'new_deaths']]
plt.boxplot(b,
            vert = True,
            whis = 3,
            patch_artist = False,
            meanline = True,
            showmeans = True,
            showbox = True,
            showcaps = True,
            showfliers = False,
            notch = False
                )
plt.title('the boxplot 1')# Name the boxplot.
plt.show()
china_dates = china_new_data.loc [:,'date']
china_new_cases = china_new_data.loc[:,'new_cases']
china_new_deaths = china_new_data.loc[:,'new_deaths']# Create three new lists.
plt.plot(china_dates, china_new_cases, 'bo')# New cases are represented by blue dots.
plt.plot(china_dates, china_new_deaths, 'r+')# Use a red '+' sign to indicate new deaths.
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-90)
# This code makes the date display one day every four days, which prevents the X-axis from being too dense.
# This code rotates the content of the X-axis by ninety degrees.
plt.xlabel('dates')# Name the X-axis.
plt.ylabel('new cases(or new deaths)of China')# Name the X-axis and the Y-axis.
plt.title('Compare new cases and new deaths in China')# Name the plot.
plt.show()

# The question starts here
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
# Change the working directory to where the full_data.csv file is stored.
os.chdir("C:/cygwin64/home/lenovo/practical7")
covid_data = pd.read_csv("full_data(2).csv")
n = 0
while n<7996:# According to the info. command, the file contains 7,996 lines.
        if covid_data.loc[n, "location"] == "Afghanistan": # Filter the row whose title is Afghanistan.
            covid_data.loc[n, "location"] = True
        else:
            covid_data.loc[n, "location"] = False
        Rows = list(covid_data.loc[:, "location"]) # Create and print a list containing the previously printed True/False.
        n+=1
# These steps are similar to the previous code for finding Afghanistan-related data.
Af_new_data = covid_data.loc[Rows,"new_cases"]
print(Af_new_data)
print(Af_new_data.mean())
# calculate the average   mean=1.7195121951219512