import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
data = pd.read_csv('llamadas_100k.csv')


data['Fraude'] = data['Fraude'].apply(lambda x: 1 if x == 'Fraudulenta' else 0)
data['Día de la semana'] = pd.Categorical(data['Día de la semana'], categories=['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'], ordered=True)


summary = data.describe()
summary.to_csv('resumen_de_datos.csv', index=False)


summary_by_operator = data.groupby('Operador', observed=False).describe()
summary_by_call_type = data.groupby('Tipo de llamada', observed=False).describe()
summary_by_operator.to_csv('resumen_por_operador.csv')
summary_by_call_type.to_csv('resumen_por_tipo_llamada.csv')


plt.hist(data['Duración'], bins=14, color='skyblue', edgecolor='black')
plt.title('Histograma de la Duración de las Llamadas')
plt.xlabel('Duración (minutos)')
plt.ylabel('Frecuencia')
plt.savefig('histograma_duracion_llamadas.png')
plt.show()


fraud_counts = data['Fraude'].value_counts()
fraud_counts.plot(kind='pie', labels=['No Fraudulentas', 'Fraudulentas'], autopct='%1.1f%%', colors=['lightgreen', 'salmon'])
plt.title('Distribución de Llamadas Fraudulentas')
plt.savefig('distribucion_llamadas_fraudulentas.png')
plt.show()


avg_duration = data.groupby('Día de la semana', observed=False)['Duración'].mean()
avg_duration.plot(kind='bar', color='lightblue')
plt.title('Duración Media de Llamadas por Día de la Semana')
plt.xlabel('Día de la Semana')
plt.ylabel('Duración Media (minutos)')
plt.savefig('duracion_media_por_dia.png')
plt.show()


fraud_counts_operator = data[data['Fraude'] == 1].groupby('Operador', observed=False).size()
if not fraud_counts_operator.empty:
    fraud_counts_operator.plot(kind='bar', color='lightcoral')
    plt.title('Cantidad de Llamadas Fraudulentas por Operador')
    plt.xlabel('Operador')
    plt.ylabel('Cantidad de Llamadas Fraudulentas')
    plt.savefig('cantidad_llamadas_fraudulentas_por_operador.png')
    plt.show()
else:
    print("No hay datos de llamadas fraudulentas para generar el gráfico.")


avg_duration_operator = data.groupby('Operador', observed=False)['Duración'].mean()
avg_duration_operator.plot(kind='bar', color='lightblue')
plt.title('Duración Media de Llamadas por Operador')
plt.xlabel('Operador')
plt.ylabel('Duración Media (minutos)')
plt.savefig('duracion_media_por_operador.png')
plt.show()


avg_duration_call_type = data.groupby('Tipo de llamada', observed=False)['Duración'].mean()
avg_duration_call_type.plot(kind='bar', color='lightgreen')
plt.title('Duración Media de Llamadas por Tipo de Llamada')
plt.xlabel('Tipo de Llamada')
plt.ylabel('Duración Media (minutos)')
plt.savefig('duracion_media_por_tipo_llamada.png')
plt.show()

# Reporte detallado
with open('reporte_detallado.txt', 'w') as f:
    f.write("Resumen de Datos:\n")
    f.write(summary.to_string())
    f.write("\n\nResumen por Operador:\n")
    f.write(summary_by_operator.to_string())
    f.write("\n\nResumen por Tipo de Llamada:\n")
    f.write(summary_by_call_type.to_string())
