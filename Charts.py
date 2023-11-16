import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ["اندازه نمایه","زمان ساخت نمایه", "زمان جستوجو","تعداد اسناد بازیابی شده"]
men_means = [0.8, 0.42, 0.549, 0.21]
women_means = [1.688, 1.59, 0.605, 0.4653]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='فری')
rects2 = ax.bar(x + width/2, women_means, width, label='اناه')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()
