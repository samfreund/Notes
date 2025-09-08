"""
1) What was the acceleration of your car during the first linear portion of the data?
The acceleration of the car in the first portion of the data can be determined by calculating 
the slope of the linear regression line. In this case, that slope is equal to 3.64 m/s^2.
"""

"""
2) What final velocity did the car approach as time approached 20 seconds?
The final velocity of the car as time approached 20 seconds is approximately 45.99 m/s.
"""

"""
3) Summarize your results by describing the motion of this car in a sentence.
The car initially accelerates at a rate of 3.64 m/s^2, reaching a final velocity of 
approximately 45.99 m/s as time approaches 20 seconds. As it approaches that final velocity,
the acceleration decreases, eventually leveling off. This results in a graph with a concave down shape.
"""

import csv
import matplotlib.pyplot as plt

values = []
with open('physics/1110/labs/lab2/values.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        values.append(row)

# Skip header
parsedValues = values[1:]

# Use a linear regression to fit to the first portion of the data
def linear_regression(data):
    n = len(data)
    sum_x = sum(int(row[0]) for row in data)
    sum_y = sum(float(row[1]) for row in data)
    sum_xy = sum(int(row[0]) * float(row[1]) for row in data)
    sum_x2 = sum(int(row[0])**2 for row in data)

    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
    intercept = (sum_y - slope * sum_x) / n
    return slope, intercept

slope, intercept = linear_regression(parsedValues[:8]) # Fit to the first 8 data points
print(f"Slope: {slope}, Intercept: {intercept}")

# Graph data using data points

x = [int(row[0]) for row in parsedValues]
speed = [float(row[1]) for row in parsedValues]

plt.scatter(x, speed, label='Speed', marker='o')

# Plot the linear regression line
regression_line = [slope * xi + intercept for xi in x]
plt.plot(x, regression_line, color='red', label='Linear Regression Fit')

plt.xlabel('Time (s)')
plt.ylabel('Speed (m/s)')
plt.title('Car Speed Over Time')
plt.xticks(range(min(x), max(x)+1, 1))
plt.legend()
plt.show()
