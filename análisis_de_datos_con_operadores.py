import pandas as pd

# Cargar datos
data = pd.read_csv('llamadas_con_operador.csv')

# Preprocesamiento de datos
data['Fraude'] = data['Fraude'].apply(lambda x: 1 if x == 'Fraudulenta' else 0)
data['Día de la semana'] = pd.Categorical(data['Día de la semana'], categories=['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'], ordered=True)

# Estadísticas descriptivas
summary = data.describe()

# Guardar estadísticas descriptivas
summary.to_csv('resumen_de_datos.csv', index=False)

print(summary)
