import matplotlib.pyplot as plt
import csv

time= []
bpm = []

with open('Output.csv', newline='') as csvread:
    plots = csvread.reader(csvread, delimiter = ' ')
    for row in plots:
        time.append(float(row[0]))
        bpm.append(float(row[4]))

plt.plot(time, bpm)
plt.show()