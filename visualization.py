import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
data = pd.read_csv('calls_data.csv')

# Gráfico de barras de duración media de llamadas por día de la semana
avg_duration = data.groupby('day_of_week')['duration'].mean()
avg_duration.plot(kind='bar')
plt.title('Duración Media de Llamadas por Día de la Semana')
plt.xlabel('Día de la Semana')
plt.ylabel('Duración Media (minutos)')
plt.savefig('avg_duration_per_day.png')
plt.show()

# Gráfico circular de llamadas fraudulentas vs. no fraudulentas
fraud_counts = data['fraud'].value_counts()
fraud_counts.plot(kind='pie', labels=['No Fraudulentas', 'Fraudulentas'], autopct='%1.1f%%')
plt.title('Distribución de Llamadas Fraudulentas')
plt.savefig('fraud_pie_chart.png')
plt.show()
