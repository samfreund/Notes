import matplotlib.pyplot as plt

data = [0.65, 0.76, 0.71, 0.75, 0.81, 0.8, 0.7, 0.73, 0.85, 0.81, 0.78, 0.75, 0.81, 0.8, 0.7, 0.83,
        0.75, 0.91, 0.96, 0.81, 0.93, 0.88, 0.85, 0.81, 0.81, 0.73, 0.95, 0.81, 0.83, 0.81, 0.85]

# Calculate avg mean time

avg_time = sum(data) / len(data)

print(f"Average Mean Time: {avg_time:.3f} seconds")

# Calculate standard deviation

squared_diffs = [(x - avg_time) ** 2 for x in data]
std_dev = (sum(squared_diffs) / len(data)) ** 0.5

print(f"Standard Deviation: {std_dev:.3f} seconds")

# Percentage of data within one standard deviation

within_one_std = [x for x in data if (avg_time - std_dev) <= x <= (avg_time + std_dev)]
percentage_within_one_std = (len(within_one_std) / len(data)) * 100

print(f"Percentage of data within one standard deviation: {percentage_within_one_std:.3f}%")

# Graph data

plt.hist(data, bins=10, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(x=avg_time, color='r', linestyle='--', label='Average Mean Time')
plt.axvspan(avg_time - std_dev, avg_time + std_dev, color='gray', alpha=0.2, label='1 Std Dev')
plt.title('Histogram of Mean Time Data')
plt.xlabel('Mean Time (seconds)')
plt.ylabel('Frequency')
plt.legend()
plt.grid()
plt.show()
