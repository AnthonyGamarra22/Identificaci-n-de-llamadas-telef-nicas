import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
data = pd.read_csv('llamadas.csv')

# Gráfico de barras de duración media de llamadas por día de la semana
avg_duration = data.groupby('Día de la semana')['Duración'].mean()
avg_duration.plot(kind='bar', color='skyblue')
plt.title('Duración Media de Llamadas por Día de la Semana')
plt.xlabel('Día de la Semana')
plt.ylabel('Duración Media (minutos)')
plt.savefig('duracion_media_por_dia.png')
plt.show()

# Gráfico circular de llamadas fraudulentas vs. no fraudulentas
fraud_counts = data['Fraude'].value_counts()
fraud_counts.plot(kind='pie', labels=['No Fraudulentas', 'Fraudulentas'], autopct='%1.1f%%', colors=['lightgreen', 'salmon'])
plt.title('Distribución de Llamadas Fraudulentas')
plt.savefig('distribucion_llamadas_fraudulentas.png')
plt.show()
