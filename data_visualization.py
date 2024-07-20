import matplotlib.pyplot as plt

# Datos de ejemplo
labels = 'Fraudulentas', 'No_Fraudulentas'
sizes = [60, 40]
colors = ['gold', 'lightcoral']
explode = (0.1, 0)

# Gráfico Circular
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.savefig('circular_chart.png')
plt.show()

# Datos de ejemplo para gráfico de barras
labels = ['Period 1', 'Period 2', 'Period 3']
Fraudulentas = [30, 25, 35]
No_Fraudulentas = [70, 75, 65]

x = range(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x, Fraudulentas, width, label='Fraudulent')
rects2 = ax.bar([p + width for p in x], No_Fraudulentas, width, label='Non-Fraudulent')

ax.set_ylabel('Frequency')
ax.set_title('Frequency of calls by period and type')
ax.set_xticks([p + width / 2 for p in x])
ax.set_xticklabels(labels)
ax.legend()

plt.savefig('bar_chart.png')
plt.show()

# Ojiva
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
plt.hist(data, bins=10, cumulative=True, histtype='step', label='Cumulative')

plt.savefig('ogive_chart.png')
plt.show()
