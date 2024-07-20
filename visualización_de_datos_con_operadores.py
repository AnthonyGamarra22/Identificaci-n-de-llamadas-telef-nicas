import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
data = pd.read_csv('llamadas_con_operador.csv')

# Asegurarse de que los datos fueron leídos correctamente
print(data.head())

# Histograma de la duración de las llamadas
plt.hist(data['Duración'], bins=14, color='skyblue', edgecolor='black')
plt.title('Histograma de la Duración de las Llamadas')
plt.xlabel('Duración (minutos)')
plt.ylabel('Frecuencia')
plt.savefig('histograma_duracion_llamadas.png')
plt.show()

# Gráfico circular de llamadas fraudulentas vs. no fraudulentas
fraud_counts = data['Fraude'].value_counts()
fraud_counts.plot(kind='pie', labels=['No Fraudulentas', 'Fraudulentas'], autopct='%1.1f%%', colors=['lightgreen', 'salmon'])
plt.title('Distribución de Llamadas Fraudulentas')
plt.savefig('distribucion_llamadas_fraudulentas.png')
plt.show()

# Gráfico de barras de duración media de llamadas por día de la semana
avg_duration = data.groupby('Día de la semana')['Duración'].mean()
avg_duration.plot(kind='bar', color='lightblue')
plt.title('Duración Media de Llamadas por Día de la Semana')
plt.xlabel('Día de la Semana')
plt.ylabel('Duración Media (minutos)')
plt.savefig('duracion_media_por_dia.png')
plt.show()

# Gráfico de barras de cantidad de llamadas fraudulentas por operador
fraud_counts_operator = data[data['Fraude'] == 1].groupby('Operador').size()
if not fraud_counts_operator.empty:
    fraud_counts_operator.plot(kind='bar', color='lightcoral')
    plt.title('Cantidad de Llamadas Fraudulentas por Operador')
    plt.xlabel('Operador')
    plt.ylabel('Cantidad de Llamadas Fraudulentas')
    plt.savefig('cantidad_llamadas_fraudulentas_por_operador.png')
    plt.show()
else:
    print("No hay datos de llamadas fraudulentas para generar el gráfico.")
