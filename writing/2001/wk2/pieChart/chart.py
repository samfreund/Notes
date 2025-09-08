import matplotlib.pyplot as plt

# Example data: time spent (in hours)
labels = ['Sleep', 'Classes', 'Exercise', 'Meals', 'Studying', 'Leisure']
sizes = [8, 5, 1, 2, 6, 2]

plt.figure(figsize=(6, 6))
wedges, texts, autotexts = plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    textprops={'fontsize': 14}  # Increase label and autopct font size
)
plt.title('How My Time is Spent Over a Day', fontsize=18)
plt.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
plt.show()
