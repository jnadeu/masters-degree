import matplotlib.pyplot as plt

# Data
algorithms = ['Random', 'GBFS']
win_rates = [12, 88]
avg_time = [0.09, 10.89]
total_time = [0.0695, 0.0478]

# Create figure and axis
fig, ax = plt.subplots(2, 1, figsize=(8, 8))

# Bar chart for Win Rate
ax[0].bar(algorithms, win_rates, color=['blue', 'orange'])
ax[0].set_title('Win Rate')
ax[0].set_ylabel('Win Rate (%)')

# Bar chart for Average Time per Move
ax[1].bar(algorithms, avg_time, color=['blue', 'orange'])
ax[1].set_title('Average Time per Move')
ax[1].set_ylabel('Time (milliseconds)')



plt.tight_layout()
plt.show()


